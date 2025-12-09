# DevOps CI/CD Pipeline Completa

Pipeline automatizado con un solo archivo YAML que realiza:

## ✅ Funcionalidades:
1. **CI:** Pruebas automáticas en cada push
2. **CD:** Build y push de imagen Docker a Docker Hub
3. **Deploy:** Despliegue automático a Render.com

## 🛠️ Configuración necesaria:

### Secrets en GitHub (Settings → Secrets and variables → Actions):
| Secret | Valor |
|--------|-------|
| `DOCKER_USERNAME` | `brayant002` |
| `DOCKER_PASSWORD` | Token de Docker Hub |
| `RENDER_API_KEY` | API Key de Render.com |

### En Docker Hub:
1. Ve a https://hub.docker.com/settings/security
2. Crea Access Token con permisos de lectura/escritura

### En Render.com:
1. Regístrate en https://render.com
2. Ve a Dashboard → Account Settings → API Keys
3. Crea nueva API Key

## 🚀 URLs del proyecto:
- **GitHub Repo:** `https://github.com/brayant002/devops-practice-cicd`
- **Docker Hub:** `https://hub.docker.com/r/brayant002/devops-cicd-app`
- **Render App:** `https://devops-cicd-app.onrender.com`

## 📁 Estructura del proyecto: