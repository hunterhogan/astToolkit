"""
Universal pytest module for any Python project.
Drop this file into your project's tests/ directory and run with: pytest test_basic.py
"""

from pathlib import Path
from typing import Any
import ast
import pytest
import subprocess
import tomllib

class ProjectAnalyzer:
    """Analyzes project structure and discovers Python modules."""

    def __init__(self, root_path: Path | None = None):
        self.root = root_path if root_path is not None else Path.cwd()
        self.project_paths = self._discover_project_paths()
        self.ignored_paths = self._get_git_ignored_paths()
        self.python_files = self._find_python_files()

    def _discover_project_paths(self) -> set[Path]:
        paths: set[Path] = set()
        pyproject_path = self.root / "pyproject.toml"
        if pyproject_path.exists():
            try:
                with open(pyproject_path, "rb") as f:
                    pyproject_data = tomllib.load(f)

                if "tool" in pyproject_data and "setuptools" in pyproject_data["tool"]:
                    setuptools_config = pyproject_data["tool"]["setuptools"]
                    if "packages" in setuptools_config:
                        if "find" in setuptools_config["packages"]:
                            find_config = setuptools_config["packages"]["find"]
                            if "where" in find_config:
                                for where in find_config["where"]:
                                    paths.add(self.root / where)

                if "project" in pyproject_data:
                    project_name = pyproject_data["project"].get("name")
                    if project_name:
                        potential_src = self.root / project_name.replace("-", "_")
                        if potential_src.is_dir():
                            paths.add(potential_src)
                        src_path = self.root / "src" / project_name.replace("-", "_")
                        if src_path.is_dir():
                            paths.add(src_path)

            except Exception:
                pass

        setup_py_path = self.root / "setup.py"
        if setup_py_path.exists():
            try:
                with open(setup_py_path, "r", encoding="utf-8") as f:
                    content = f.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                        if node.func.id == "setup":
                            for keyword in node.keywords:
                                if keyword.arg == "package_dir":
                                    if isinstance(keyword.value, ast.Dict):
                                        for _key_node, value_node in zip(keyword.value.keys, keyword.value.values):
                                            if isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                                                paths.add(self.root / value_node.value)
                                elif keyword.arg == "packages":
                                    if isinstance(keyword.value, ast.List):
                                        for pkg_node in keyword.value.elts:
                                            if isinstance(pkg_node, ast.Constant) and isinstance(pkg_node.value, str):
                                                pkg_path = self.root / pkg_node.value.replace(".", "/")
                                                if pkg_path.is_dir():
                                                    paths.add(pkg_path)
            except Exception:
                pass

        if not paths:
            common_layouts = [self.root / "src", self.root]
            for layout_path in common_layouts:
                if layout_path.is_dir():
                    for item in layout_path.iterdir():
                        if item.is_dir() and (item / "__init__.py").exists() and not item.name.startswith("."):
                            paths.add(item)

        return paths or {self.root}

    def _get_git_ignored_paths(self) -> set[Path]:
        ignored: set[Path] = set()
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                cwd=self.root,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                result = subprocess.run(
                    ["git", "status", "--ignored", "--porcelain"],
                    cwd=self.root,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if result.returncode == 0:
                    for line in result.stdout.splitlines():
                        if line.startswith("!! "):
                            ignored_path = self.root / line[3:]
                            ignored.add(ignored_path)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        common_ignored = [
            "__pycache__", ".pytest_cache", ".git", ".venv", "venv", ".env",
            "node_modules", ".tox", "build", "dist"
        ]

        for pattern in common_ignored:
            for path in self.root.rglob(pattern):
                ignored.add(path)

        return ignored

    def _find_python_files(self) -> list[Path]:
        python_files: list[Path] = []
        for project_path in self.project_paths:
            if not project_path.exists():
                continue
            for py_file in project_path.rglob("*.py"):
                if any(py_file.is_relative_to(ignored) for ignored in self.ignored_paths if ignored.exists()):
                    continue
                if "test" in py_file.name.lower() or "test" in str(py_file.parent).lower():
                    continue
                python_files.append(py_file)
        return python_files

    def analyze_file(self, file_path: Path) -> dict[str, Any]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return {"path": file_path, "size": len(content), "lines": len(content.splitlines()), "syntax_valid": True}
        except SyntaxError:
            return {"path": file_path, "syntax_valid": False, "error": "Syntax error in file"}
        except Exception as e:
            return {"path": file_path, "syntax_valid": False, "error": str(e)}


analyzer = ProjectAnalyzer()


class TestBasicStructure:
    def test_has_python_files(self):
        assert analyzer.python_files, "No Python files found"

    def test_root_has_config_file(self):
        pyproject = (analyzer.root / "pyproject.toml").exists()
        setup = (analyzer.root / "setup.py").exists()
        assert pyproject or setup, "Missing pyproject.toml or setup.py"

    @pytest.mark.parametrize("file_path", analyzer.python_files)
    def test_valid_syntax(self, file_path: Path):
        analysis = analyzer.analyze_file(file_path)
        assert analysis["syntax_valid"], f"Syntax error in {file_path}: {analysis.get('error', '')}"

    def test_has_readme(self):
        readmes = ["README.md", "README.rst", "README.txt", "README"]
        assert any((analyzer.root / r).exists() for r in readmes), "No README file found"

    def test_python_version_specified(self):
        version_specified = False
        pyproject = analyzer.root / "pyproject.toml"
        if pyproject.exists():
            try:
                with open(pyproject, "rb") as f:
                    data = tomllib.load(f)
                version_specified = "project" in data and "requires-python" in data["project"]
            except Exception:
                pass
        if not version_specified:
            setup = analyzer.root / "setup.py"
            if setup.exists():
                try:
                    with open(setup, "r", encoding="utf-8") as f:
                        content = f.read()
                    version_specified = "python_requires" in content
                except Exception:
                    pass
        if not version_specified:
            pytest.skip("No Python version specified")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
