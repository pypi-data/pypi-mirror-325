import os
import subprocess
import sys
import importlib.util


def main():

    # Vérifier la version de Python
    if sys.version_info < (3, 9):
        print("Python 3.9+ est requis pour ce script.")
        sys.exit(1)

    if importlib.util.find_spec("django") is None:
        print("Django n'est pas installé. Veuillez l'installer avec :")
        print("pip install django")
        sys.exit(1)

    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True, check=True)
        version = result.stdout.strip()

        if version.startswith("v20."):
            print(f"✅ Node.js {version} est installé.")
        else:
            print(f"⚠️ Node.js {version} est installé, mais ce n'est pas la version 20.")
            sys.exit(1)
    except FileNotFoundError:
        print("❌ Node.js n'est pas installé.")
        sys.exit(1)

    # Fonction pour exécuter une commande
    def run_command(command, cwd=None, shell=True):

        result = subprocess.run(command, cwd=cwd, shell=shell, text=True)
        if result.returncode != 0:
            print(f"❌ Erreur lors de l'exécution de : {command}")
            sys.exit(1)

    # 📌 Étape 1 : Demander le nom du projet
    project_name = input("📦 Nom du projet (default: django-vite-app) : ").strip() or "django-vite-app"

    # 📌 Étape 2 : Choisir les modules Django
    print("\n🔧 Sélectionne les modules Django à installer :")
    django_modules = {
        "1": "djangorestframework",
        "2": "django-cors-headers",
    }
    selected_modules = []
    for key, module in django_modules.items():
        choice = input(f"  [{key}] {module} (y/N) : ").strip().lower()
        if choice == "y":
            selected_modules.append(module)

    # 📌 Étape 3 : Choisir le frontend
    print("\n🎨 Choisis un framework frontend :")
    frontend_choices = {
        "1": "react",
    }
    frontend_choice = input("  [1] React (default: React) : ").strip() or "1"
    frontend = frontend_choices.get(frontend_choice, "react")


    # 📌 Étape 5 : Installer Tailwind ?
    install_tailwind = input("\n🎨 Installer Tailwind CSS ? (Y/n) : ").strip().lower() or "y"

    # 📌 Étape 6 : Initialiser Git ?
    init_git = input("\n🔗 Initialiser Git ? (Y/n) : ").strip().lower() or "y"

    # Définir les chemins
    base_dir = os.path.abspath(project_name)
    backend_dir = os.path.join(base_dir, "backend")
    frontend_dir = os.path.join(base_dir, "frontend")

    # 📂 Création des dossiers
    print("\n📂 Création des dossiers...")
    os.makedirs(backend_dir, exist_ok=True)
    os.makedirs(frontend_dir, exist_ok=True)

    # 🐍 Installation du backend Django
    print("\n🐍 Installation du backend Django...")
    os.chdir(backend_dir)
    run_command("python -m venv venv")
    venv_python = os.path.join(backend_dir, "venv", "Scripts", "python.exe" if os.name == "nt" else "bin/python")
    run_command(f"{venv_python} -m pip install django {' '.join(selected_modules)}")
    run_command(f"{venv_python} -m django startproject core .")

    # 📜 Modifier settings.py
    settings_path = os.path.join(backend_dir, "core", "settings.py")
    with open(settings_path, "r") as file:
        settings = file.readlines()

    if "djangorestframework" in selected_modules:
        settings.append("\nINSTALLED_APPS.append('rest_framework')")


    if "django-cors-headers" in selected_modules:
        settings.append("\nINSTALLED_APPS.append('corsheaders')")
        settings.insert(settings.index("MIDDLEWARE = [\n") + 1, "    'corsheaders.middleware.CorsMiddleware',\n")
        settings.append("\nCORS_ALLOWED_ORIGINS = [\n    'http://localhost:5173',\n]\n")

    with open(settings_path, "w") as file:
        file.writelines(settings)



    # ✅ Fin de l'installation
    print("\n✅ Installation terminée du backend Terminer!")



    # ⚛️ Installation du frontend avec Vite
    print(f"\n⚛️ Installation du frontend avec Vite ({frontend})...")
    os.chdir(frontend_dir)
    run_command(f"npm create vite@latest . -- --template {frontend}")
    run_command("npm install")

    # 📦 Installation de Tailwind CSS (si choisi)
    if install_tailwind == "y":
        print("\n🎨 Installation de Tailwind CSS...")
        run_command("npm install -D tailwindcss@3.4.17 postcss@8.4.21 autoprefixer@10.4.14")
        run_command("npx tailwindcss init -p")


        # Ajout de la configuration Tailwind
        with open("tailwind.config.js", "w") as file:
            file.write("""export default {
            content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
            theme: { extend: {} },
            plugins: [],
            }""")

        # Mise à jour du fichier CSS principal
        styles_path = "src/index.css" if frontend == "react" else "src/main.css"

        custom_styles = """\
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
    
    
    
        :root {
        font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
        line-height: 1.5;
        font-weight: 400;
    
        color-scheme: light dark;
        color: rgba(255, 255, 255, 0.87);
        background-color: #242424;
    
        font-synthesis: none;
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        }
    
        a {
        font-weight: 500;
        color: #646cff;
        text-decoration: inherit;
        }
        a:hover {
        color: #535bf2;
        }
    
        body {
        margin: 0;
        display: flex;
        place-items: center;
        min-width: 320px;
        min-height: 100vh;
        }
    
        h1 {
        font-size: 3.2em;
        line-height: 1.1;
        }
    
        button {
        border-radius: 8px;
        border: 1px solid transparent;
        padding: 0.6em 1.2em;
        font-size: 1em;
        font-weight: 500;
        font-family: inherit;
        background-color: #1a1a1a;
        cursor: pointer;
        transition: border-color 0.25s;
        }
        button:hover {
        border-color: #646cff;
        }
        button:focus,
        button:focus-visible {
        outline: 4px auto -webkit-focus-ring-color;
        }
    
        @media (prefers-color-scheme: light) {
        :root {
            color: #213547;
            background-color: #ffffff;
        }
        a:hover {
            color: #747bff;
        }
        button {
            background-color: #f9f9f9;
        }
        }
    
        """

        # Écriture des styles personnalisés AVANT Tailwind
        with open(styles_path, "w") as file:
            file.write(custom_styles)


    # 🛠️ Configuration vite.config.js
    vite_config = f"""import {{ defineConfig }} from 'vite'
    import {frontend} from '@vitejs/plugin-{frontend}'
    
    export default defineConfig({{
      plugins: [{frontend}()],
      server: {{
        proxy: {{
          '/api': {{
            target: 'http://localhost:8000',
            changeOrigin: true,
            secure: false
          }}
        }}
      }}
    }})
    """
    with open("vite.config.js", "w") as file:
        file.write(vite_config)

    # 🔗 Initialisation Git (si choisi)
    if init_git == "y":
        print("\n🛠️ Initialisation de Git...")
        os.chdir(base_dir)
        run_command("git init")

        gitignore_content = """# Django
                    venv/
                    *.pyc
                    .env
                    db.sqlite3
    
                    # Vite
                    node_modules/
                    dist/
                    .env
                    """
        with open(".gitignore", "w") as file:
            file.write(gitignore_content)


    # ✅ Fin de l'installation
    print("\n✅ Installation terminée !")
    print(f"👉 Commandes :")
    print(f" - Backend : cd {project_name}/backend && venv\\Scripts\\activate && python manage.py migrate && python manage.py runserver")
    print(f" - Frontend : cd {project_name}/frontend && npm run dev")
