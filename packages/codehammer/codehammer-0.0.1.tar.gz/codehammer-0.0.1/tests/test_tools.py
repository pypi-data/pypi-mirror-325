import os
from pathlib import Path
import pytest
from codehammer.core.main import (
    CodeHammer,
)
from langchain_core.tools import BaseTool

# -----------------------------------------------------------------------------
# Fixtures: Create a temporary environment and a CodeHammer instance.
# -----------------------------------------------------------------------------

@pytest.fixture
def temp_env(tmp_path):
    """
    Create a temporary directory structure for testing.
      - A file "a.txt" at the root.
      - A subdirectory "sub" with a file "b.txt".
    """
    base_dir = tmp_path / "test_dir"
    base_dir.mkdir()
    # Create a text file in the root
    (base_dir / "a.txt").write_text("Content A", encoding="utf-8")
    # Create a subdirectory with a file
    sub_dir = base_dir / "sub"
    sub_dir.mkdir()
    (sub_dir / "b.txt").write_text("Content B", encoding="utf-8")
    # Return the base directory path as a string
    return str(base_dir)

@pytest.fixture
def hammer(temp_env):
    """
    Create a CodeHammer instance using the temporary environment.
    Set an output file (combined.txt) and force overwrite.
    """
    output_file = os.path.join(temp_env, "combined.txt")
    return CodeHammer(base_dir=temp_env, output_file=output_file, force=True)

@pytest.fixture
def tools(hammer):
    """
    Return a dictionary mapping tool names to tool instances, using the
    get_tools() method of CodeHammer.
    """
    tool_list = hammer.get_tools()
    return {tool.name: tool for tool in tool_list}

# -----------------------------------------------------------------------------
# Test each tool returned by get_tools()
# -----------------------------------------------------------------------------

def test_get_directory_tree_tool(tools, temp_env):
    tool = tools.get("get_directory_tree")
    # Calling with folder_path "." should list files relative to base_dir.
    result = tool._run(folder_path=".")
    # Check that the file "a.txt" and the nested file "sub/b.txt" are included.
    assert isinstance(result, list)
    # Because of different path formatting, we check substrings.
    assert any("a.txt" in path for path in result)
    assert any("sub" in path and "b.txt" in path for path in result)

def test_get_file_content_tool(tools, temp_env):
    tool = tools.get("get_file_content")
    # Retrieve the content of "a.txt".
    result = tool._run(file_path="a.txt")
    assert result == "Content A"

def test_get_files_in_folder_tool(tools, temp_env):
    tool = tools.get("get_files_in_folder")
    # Get files in the "sub" folder.
    result = tool._run(folder_path="sub")
    assert isinstance(result, dict)
    assert "b.txt" in result
    assert result["b.txt"] == "Content B"

def test_get_files_recursively_tool(tools, temp_env):
    tool = tools.get("get_files_recursively")
    # Request all files under the base directory.
    result = tool._run(folder_path=".")
    # Expect both "a.txt" and a file from the subdirectory.
    keys = list(result.keys())
    assert any("a.txt" in key for key in keys)
    assert any("sub" in key and "b.txt" in key for key in keys)

def test_find_files_tool(tools, temp_env):
    tool = tools.get("find_files")
    # Find all files with extension "txt".
    result = tool._run(extensions=["txt"])
    assert isinstance(result, list)
    # Extract just the filenames.
    file_names = [Path(p).name for p in result]
    assert "a.txt" in file_names
    assert "b.txt" in file_names

def test_write_file_tool(tools, temp_env):
    tool = tools.get("write_file")
    # Write content to "test_out.txt" inside the .result folder.
    result = tool._run(file_path="test_out.txt", content="Test write")
    # Check that the file exists in the .result folder.
    result_file = Path(temp_env) / ".result" / "test_out.txt"
    assert result_file.exists()
    assert result_file.read_text(encoding="utf-8") == "Test write"
    assert "File written successfully:" in result

def test_clean_result_folder_tool(tools, temp_env):
    # First, create a file in the .result folder.
    result_dir = Path(temp_env) / ".result"
    result_dir.mkdir(exist_ok=True)
    file_to_remove = result_dir / "remove.txt"
    file_to_remove.write_text("Delete me", encoding="utf-8")
    
    tool = tools.get("clean_result_folder")
    # Run the tool to remove "remove.txt".
    tool._run(excluded_files=["remove.txt"])
    assert not file_to_remove.exists()

def test_forge_prompt_tool(tools, temp_env):
    tool = tools.get("forge_prompt")
    base_path = Path(temp_env)
    # Create two Python files to combine.
    (base_path / "file1.py").write_text("print('Hello from file1')", encoding="utf-8")
    (base_path / "file2.py").write_text("print('Hello from file2')", encoding="utf-8")
    # Call forge_prompt on the extension "py".
    tool._run(extensions=["py"])
    output_file = base_path / "combined.txt"
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "print('Hello from file1')" in content
    assert "print('Hello from file2')" in content

def test_run_tool(tools, temp_env):
    tool = tools.get("run")
    base_path = Path(temp_env)
    # Create a Python file to be processed.
    (base_path / "file3.py").write_text("print('Run tool test')", encoding="utf-8")
    # Call the run tool; it should internally call forge_prompt.
    tool._run(extensions=["py"])
    output_file = base_path / "combined.txt"
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "print('Run tool test')" in content

def test_duckduckgo_tools(tools):
    # For the network-based tools, we test that they exist and are instances of BaseTool.
    ddg_run = tools.get("duckduckgo_search")
    ddg_results = tools.get("duckduckgo_results_json")
    assert isinstance(ddg_run, BaseTool)
    assert isinstance(ddg_results, BaseTool)