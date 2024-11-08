import collections
import unittest
from bisect import bisect_left, insort


class FileSystem:
    def __init__(self) -> None:
        self.paths = collections.defaultdict(list)
        self.files = {}

    def ls(self, path: str) -> list[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        else:
            return self.paths.get(path, [])

    def mkdir(self, path: str) -> None:
        directories = path.strip('/').split('/')
        current_path = ''
        for directory in directories:
            current_path += '/' + directory
            if current_path not in self.paths:
                self.paths[current_path] = []
                # Add this directory to its parent directory
                parent_path = current_path.rsplit('/', 1)[0] or '/'
                if parent_path not in self.paths:
                    self.paths[parent_path] = []
                if directory not in self.paths[parent_path]:
                    insort(self.paths[parent_path], directory)

    # touch and vi
    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            # Ensure the parent directories exist
            parent_path = filePath.rsplit('/', 1)[0] or '/'
            self.mkdir(parent_path)
            file_name = filePath.split('/')[-1]
            if file_name not in self.paths[parent_path]:
                insort(self.paths[parent_path], file_name)
            self.files[filePath] = ''
        self.files[filePath] += content

    # cat
    def readContentFromFile(self, filePath: str) -> str:
        if filePath in self.files:
            return self.files[filePath]


    def display_file(self):
        print(self.files)

    def display_directory(self):
        print(self.paths)


class TestFileSystem(unittest.TestCase):
    def test_file_system(self):
        fs = FileSystem()
        # fs.mkdir("/a/b/c")
        fs.mkdir("/a/b/d")
        fs.mkdir("/a/b/e")
        fs.addContentToFile("/a/b/c/file", "hello")
        fs.addContentToFile("/a/b/c/another", "hello")
        # fs.addContentToFile("/a/b/e/f", "world")
        # print(fs.ls("/a/b/c"))
        # print(fs.ls("/a"))
        # print(fs.ls("/"))
        print(fs.ls("/a/b/c/file"))
        print(fs.ls("/a/b/c/another"))
        print(fs.ls("/a/b"))
        # self.assertEqual(fs.ls("/a"), ["b"])
        # self.assertEqual(fs.ls("/a/b"), ["c"])
        # self.assertEqual(fs.ls("/a/b/c"), [])
        # fs.addContentToFile("/a/b/c/d", "hello")
        # self.assertEqual(fs.readContentFromFile("/a/b/c/d"), "hello")
        # self.assertEqual(fs.ls("/a/b/c"), ["d"])
        fs.display_file()
        fs.display_directory()


if __name__ == "__main__":
    unittest.main()
