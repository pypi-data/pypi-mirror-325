import json
import os
from pathlib import Path
from .base import DockerfileGenerator
from .exceptions import InvalidPackageJsonError

class NodeJSGenerator(DockerfileGenerator):
    def __init__(self, app_path):
        super().__init__(app_path)
        self.package_json = self._load_package_json()
        self.node_version = self._detect_node_version()
        self.framework = self._detect_framework()

    def _load_package_json(self):
        path = Path(self.app_path) / "package.json"
        try:
            with open(path) as f:
                return json.load(f)
        except (json.JSONDecoderError, FileNotFoundError) as e:
            raise InvalidPackageJsonError(f"Invalid package.json")

    def _detect_node_version(self):
        return self.package_json.get("engines", {}).get("node", "18")

    def _detect_framework(self):
        dependencies = self.package_json.get("dependencies", {})
        dev_dependencies = self.package_json.get("dev_dependencies", {})

        if "next" in dependencies or "next" in dev_dependencies:
            return "next"
        elif "nuxt" in dependencies or "nuxt" in dev_dependencies:
            return "nuxt"
        elif "react-scripts" in dependencies:
            return "create-react-app"
        elif "@nestjs/core" in dependencies:
            return "nestjs"
        elif "vue" in dependencies or "vite" in dependencies:
            return "vue"
        else:
            return "generic"

    def generate_dockerfile(self):
        self.add_from(f"node:{self.node_version}")
        self.add_workdir("/app")
        self.add_copy("package.json", ".")
        self.add_run("npm install")
        self.add_copy(".", ".")

        if self.framework == "next":
            self.add_run("npm run build")
            self.add_expose(3000)
            self.add_cmd("npm start")
        elif self.framework == "nuxt":
            self.add_run("npm run build")
            self.add_expose(5000)
            self.add_cmd("npx serve -s build")
        elif self.framework == "create-react-app":
            self.add_run("npm run build")
            self.add_expose(3000)
            self.add_cmd("node dist/main.js")
        elif self.framework == "vue":
            if "vite" in self.package_json.get("dependencies", {}):
                self.add_run("npm run build")
                self.add_expose(4137)
                self.add_cmd("npm run preview")
            else:
                self.add_expose(8000)
                self.add_cmd("npm run serve")
        else:
            self.add_expose(3000)
            self.add_cmd("npm start")

