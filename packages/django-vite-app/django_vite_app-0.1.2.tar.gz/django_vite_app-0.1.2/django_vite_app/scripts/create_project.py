import os
import subprocess
import sys
import importlib.util
import argparse
from typing import List, Dict


class ProjectCreator:
    def __init__(self):
        self.project_name = ""
        self.base_dir = ""
        self.backend_dir = ""
        self.frontend_dir = ""

    def check_requirements(self) -> None:
        """Vérifie les prérequis du système"""
        # Vérification de Python
        if sys.version_info < (3, 9):
            self.exit_with_error("Python 3.9+ est requis pour ce script.")

        # Vérification de Django
        if importlib.util.find_spec("django") is None:
            self.exit_with_error("Django n'est pas installé. Veuillez l'installer avec :\npip install django")

        # Vérification de Node.js
        try:
            result = subprocess.run(["node", "--version"], capture_output=True, text=True, check=True)
            version = result.stdout.strip()
            if not version.startswith("v20."):
                self.exit_with_error(f"Node.js {version} est installé, mais la version 20 est requise.")
            print(f"✅ Node.js {version} est installé.")
        except FileNotFoundError:
            self.exit_with_error("❌ Node.js n'est pas installé.")

    def run_command(self, command: str, cwd: str = None, shell: bool = True) -> None:
        """Exécute une commande shell avec gestion d'erreur"""
        try:
            result = subprocess.run(command, cwd=cwd, shell=shell, text=True, capture_output=True)
            if result.returncode != 0:
                self.exit_with_error(f"❌ Erreur lors de l'exécution de : {command}\n{result.stderr}")
            return result.stdout
        except Exception as e:
            self.exit_with_error(f"❌ Erreur : {str(e)}")

    def get_user_inputs(self) -> None:
        """Collecte les entrées utilisateur de manière interactive ou via arguments"""
        parser = argparse.ArgumentParser(description='Créer un projet Django avec Vite')
        parser.add_argument('--name', help='Nom du projet')
        parser.add_argument('--modules', help='Modules Django (comma-separated)')
        parser.add_argument('--no-tailwind', action='store_true', help='Ne pas installer Tailwind')
        parser.add_argument('--no-git', action='store_true', help='Ne pas initialiser Git')

        args = parser.parse_args()

        # Mode interactif si aucun argument n'est fourni
        if not any(vars(args).values()):
            self.project_name = input("📦 Nom du projet (default: django-vite-app) : ").strip() or "django-vite-app"

            print("\n🔧 Sélectionne les modules Django à installer :")
            self.selected_modules = self.select_modules()

            self.install_tailwind = input("\n🎨 Installer Tailwind CSS ? (Y/n) : ").strip().lower() != 'n'
            self.init_git = input("\n🔗 Initialiser Git ? (Y/n) : ").strip().lower() != 'n'
        else:
            self.project_name = args.name or "django-vite-app"
            self.selected_modules = args.modules.split(',') if args.modules else []
            self.install_tailwind = not args.no_tailwind
            self.init_git = not args.no_git

        self.base_dir = os.path.abspath(self.project_name)
        self.backend_dir = os.path.join(self.base_dir, "backend")
        self.frontend_dir = os.path.join(self.base_dir, "frontend")

    def setup_django_backend(self) -> None:
        """Configure le backend Django"""
        print("\n🐍 Installation du backend Django...")
        os.makedirs(self.backend_dir, exist_ok=True)
        os.chdir(self.backend_dir)

        # Création de l'environnement virtuel
        self.run_command("python -m venv venv")
        venv_python = os.path.join(self.backend_dir, "venv", "Scripts",
                                   "python.exe") if os.name == "nt" else os.path.join(self.backend_dir, "venv", "bin",
                                                                                      "python")

        # Installation des dépendances
        self.run_command(f"{venv_python} -m pip install django {' '.join(self.selected_modules)}")
        self.run_command(f"{venv_python} -m django startproject core .")

        # Configuration de settings.py
        self.update_django_settings()

    def setup_frontend(self) -> None:
        """Configure le frontend avec Vite et React"""
        print("\n⚛️ Installation du frontend avec Vite...")
        os.makedirs(self.frontend_dir, exist_ok=True)
        os.chdir(self.frontend_dir)

        self.run_command("npm create vite@latest . -- --template react")
        self.run_command("npm install")

        if self.install_tailwind:
            self.setup_tailwind()

        self.configure_vite()

    def finalize_setup(self) -> None:
        """Finalise l'installation"""
        if self.init_git:
            print("\n🛠️ Initialisation de Git...")
            os.chdir(self.base_dir)
            self.run_command("git init")
            self.create_gitignore()

        print("\n✅ Installation terminée !")
        self.print_next_steps()

    @staticmethod
    def exit_with_error(message: str) -> None:
        """Quitte le script avec un message d'erreur"""
        print(message)
        sys.exit(1)

    def create_project(self) -> None:
        """Point d'entrée principal pour la création du projet"""
        self.check_requirements()
        self.get_user_inputs()
        self.setup_django_backend()
        self.setup_frontend()
        self.finalize_setup()


def main():
    creator = ProjectCreator()
    creator.create_project()


if __name__ == "__main__":
    main()