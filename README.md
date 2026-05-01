# Automação de Google Forms com Selenium

Automatiza o preenchimento e envio de um formulário de votação livre do Google Forms usando Python, Selenium e WebDriver Manager.

## 🚀 Visão geral
Este projeto abre um formulário do Google Forms no Chrome, seleciona várias opções pré-definidas, envia o formulário e repete o processo em loop para múltiplos envios.

> Atenção: este projeto é destinado apenas a fins educacionais. Envio massivo de formulários pode violar termos de uso do Google Forms e ser bloqueado.

## ✅ Funcionalidades
- Preenchimento automático de opções específicas (select)
- Envio automático do formulário
- Retorno à página de nova submissão para múltiplos envios
- Uso de variáveis de ambiente para a URL do formulário

## 🛠️ Tecnologias
- Python 3.13+
- Selenium
- webdriver-manager
- python-dotenv

## 📦 Instalação
1. Clone este repositório:
\`\`\`bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd votando-no-ovo
\`\`\`
2. Instale as dependências:
\`\`\`bash
uv add selenium python-dotenv webdriver-manager
\`\`\`

## ⚙️ Configuração
Crie um arquivo `.env` na raiz do projeto com a URL do formulário:
\`\`\`ini
FORM_URL=https://docs.google.com/forms/d/e/SEU_FORM_AQUI/viewform
\`\`\`

Inclua `.env` no `.gitignore` para não versionar dados sensíveis.

## ▶️ Como executar
\`\`\`bash
python main.py
\`\`\`

## ⚠️ Observações importantes
- IDs de elementos do Google Forms como `i6`, `i35`, etc. podem mudar com o tempo.
- O script funciona apenas se o formulário estiver configurado com campos que correspondam aos IDs presentes em `lista_de_vencedores`.
- Envio repetitivo pode ser detectado e bloqueado pelo Google.

## 📄 Licença
Distribuído sob a licença MIT.