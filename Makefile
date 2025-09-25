# Makefile para Projeto Pokémon Elite Four
# ======================================

.PHONY: help install install-dev setup format lint test clean run-demo run-optimize run-analyze run-simulate report

# Variáveis
PYTHON = python3
PIP = pip3
VENV_DIR = venv
REQUIREMENTS = requirements.txt

# Comando padrão
help: ## Mostra esta ajuda
	@echo "Pokémon Elite Four - Comandos Disponíveis:"
	@echo "=========================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Instalação e Configuração
install: ## Instala dependências básicas
	@echo "📦 Instalando dependências..."
	$(PIP) install -r $(REQUIREMENTS)
	@echo "✅ Dependências instaladas!"

install-dev: ## Instala dependências de desenvolvimento
	@echo "🛠️  Instalando dependências de desenvolvimento..."
	$(PIP) install -r $(REQUIREMENTS)
	$(PIP) install pytest pytest-cov black flake8 isort mypy pre-commit
	@echo "✅ Dependências de desenvolvimento instaladas!"

setup: ## Configura ambiente completo (venv + deps + pre-commit)
	@echo "🚀 Configurando ambiente completo..."
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "📁 Criando ambiente virtual..."; \
		$(PYTHON) -m venv $(VENV_DIR); \
	fi
	@echo "📦 Instalando dependências no venv..."
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	$(VENV_DIR)/bin/pip install pytest pytest-cov black flake8 isort mypy pre-commit
	@echo "🔧 Configurando pre-commit..."
	$(VENV_DIR)/bin/pre-commit install || echo "⚠️  Pre-commit não configurado (opcional)"
	@echo "✅ Ambiente configurado! Use: source venv/bin/activate"

# Qualidade de Código
format: ## Formata código com black e isort
	@echo "🎨 Formatando código..."
	black --line-length 88 pokemon_elite_four/ tests/ main.py
	isort --profile black pokemon_elite_four/ tests/ main.py
	@echo "✅ Código formatado!"

lint: ## Verifica qualidade do código
	@echo "🔍 Verificando qualidade do código..."
	flake8 --max-line-length=88 --extend-ignore=E203,W503 pokemon_elite_four/ tests/ main.py
	black --check --line-length 88 pokemon_elite_four/ tests/ main.py
	isort --check-only --profile black pokemon_elite_four/ tests/ main.py
	@echo "✅ Código verificado!"

# Testes
test: ## Executa todos os testes
	@echo "🧪 Executando testes..."
	pytest tests/ -v --tb=short
	@echo "✅ Testes executados!"

test-cov: ## Executa testes com cobertura
	@echo "📊 Executando testes com cobertura..."
	pytest tests/ -v --cov=pokemon_elite_four --cov-report=html --cov-report=term
	@echo "✅ Relatório de cobertura gerado em htmlcov/"

test-quick: ## Executa testes rápidos (sem integração)
	@echo "⚡ Executando testes rápidos..."
	pytest tests/ -v -k "not integration" --tb=short
	@echo "✅ Testes rápidos executados!"

# Execução do Projeto
run-demo: ## Executa modo demonstração
	@echo "🎮 Executando modo demonstração..."
	$(PYTHON) main.py --mode demo
	@echo "✅ Demonstração concluída!"

run-optimize: ## Executa otimização de equipe
	@echo "🧬 Executando otimização de equipe..."
	$(PYTHON) main.py --mode optimize --generations 50 --population 100
	@echo "✅ Otimização concluída!"

run-analyze: ## Executa análise completa
	@echo "📊 Executando análise completa..."
	$(PYTHON) main.py --mode analyze --simulations 1000
	@echo "✅ Análise concluída!"

run-simulate: ## Executa simulações
	@echo "⚔️  Executando simulações..."
	$(PYTHON) main.py --mode simulate --simulations 500
	@echo "✅ Simulações concluídas!"

# Relatórios e Visualizações
report: ## Gera relatório completo
	@echo "📋 Gerando relatório completo..."
	$(PYTHON) -c "from pokemon_elite_four.utils.visualization import save_all_visualizations; save_all_visualizations()"
	@echo "✅ Relatório gerado em output/plots/"

notebook: ## Executa notebook Jupyter
	@echo "📓 Iniciando Jupyter Notebook..."
	jupyter notebook docs/CASE_TECNICO_38_PERGUNTAS_PYTHON.ipynb

# Limpeza
clean: ## Remove arquivos temporários
	@echo "🧹 Limpando arquivos temporários..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	find . -type f -name "*.tmp" -delete
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	@echo "✅ Limpeza concluída!"

clean-output: ## Remove arquivos de saída
	@echo "🗑️  Removendo arquivos de saída..."
	rm -rf output/logs/*
	rm -rf output/temp/*
	rm -rf output/.cache/*
	@echo "✅ Arquivos de saída removidos!"

clean-all: clean clean-output ## Limpeza completa
	@echo "🧽 Limpeza completa realizada!"

# Desenvolvimento
check: lint test ## Verifica código e executa testes
	@echo "✅ Verificação completa concluída!"

dev-setup: setup install-dev ## Configuração completa para desenvolvimento
	@echo "🎯 Ambiente de desenvolvimento pronto!"

# Informações
info: ## Mostra informações do projeto
	@echo "📋 Informações do Projeto:"
	@echo "========================="
	@echo "Nome: Pokémon Elite Four"
	@echo "Versão: 2.0.0"
	@echo "Autor: Adriano Carvalho dos Santos"
	@echo "Python: $(shell $(PYTHON) --version)"
	@echo "Pip: $(shell $(PIP) --version)"
	@echo "Diretório: $(shell pwd)"
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "Virtual Env: ✅ Configurado"; \
	else \
		echo "Virtual Env: ❌ Não configurado"; \
	fi

status: ## Mostra status do projeto
	@echo "📊 Status do Projeto:"
	@echo "===================="
	@echo "Arquivos Python: $(shell find pokemon_elite_four/ -name '*.py' | wc -l)"
	@echo "Arquivos de Teste: $(shell find tests/ -name '*.py' | wc -l)"
	@echo "Linhas de Código: $(shell find pokemon_elite_four/ -name '*.py' -exec wc -l {} + | tail -n1 | awk '{print $$1}')"
	@echo "Tamanho dos Dados: $(shell du -sh data/ 2>/dev/null || echo 'N/A')"
	@echo "Tamanho do Output: $(shell du -sh output/ 2>/dev/null || echo 'N/A')"

# Docker (opcional)
docker-build: ## Constrói imagem Docker (se Dockerfile existir)
	@if [ -f "Dockerfile" ]; then \
		echo "🐳 Construindo imagem Docker..."; \
		docker build -t pokemon-elite-four:latest .; \
		echo "✅ Imagem Docker construída!"; \
	else \
		echo "❌ Dockerfile não encontrado"; \
	fi

# Backup
backup: ## Cria backup do projeto
	@echo "💾 Criando backup..."
	@DATE=$$(date +%Y%m%d_%H%M%S); \
	tar -czf "backup_pokemon_elite_four_$$DATE.tar.gz" \
		--exclude='venv' \
		--exclude='__pycache__' \
		--exclude='*.pyc' \
		--exclude='output/logs' \
		--exclude='output/temp' \
		--exclude='.git' \
		.
	@echo "✅ Backup criado: backup_pokemon_elite_four_$$(date +%Y%m%d_%H%M%S).tar.gz"
