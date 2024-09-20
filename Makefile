# Variables globales
PYTHON = python3
TARGET = main.py
GENERATEUR = npuzzle-gen.py
CLEAN_FILES = __pycache__ puzzle.txt

# Règle par défaut
all:
	@${PYTHON} $(TARGET)

# Règle pour compiler le fichier main.py
$(TARGET):
	$(PYTHON) $(TARGET)

# Règle pour supprimer les fichiers générés
clean:
	@rm -rf $(CLEAN_FILES)

create_%:
	@$(PYTHON) $(GENERATEUR) $* > temp_puzzle.txt
	@sh script.sh
	@rm -rf temp_puzzle.txt
	@mv formatted_puzzle.txt puzzle.txt

solvable_%:
	@$(PYTHON) $(GENERATEUR) $* -s > temp_puzzle.txt
	@sh script.sh
	@rm -rf temp_puzzle.txt
	@mv formatted_puzzle.txt puzzle.txt
	@$(PYTHON) $(TARGET) puzzle.txt

unsolvable_%:
	@$(PYTHON) $(GENERATEUR) $* -u > temp_puzzle.txt
	@sh script.sh
	@rm -rf temp_puzzle.txt
	@mv formatted_puzzle.txt puzzle.txt
	@$(PYTHON) $(TARGET) puzzle.txt

use_%: create_%
	@$(PYTHON) $(TARGET) puzzle.txt

use :
	@$(PYTHON) $(TARGET) puzzle.txt

# Règle pour supprimer les fichiers générés et recompiler
fclean: clean

re: fclean all

# Règle factice pour éviter les conflits avec des fichiers portant le même nom
.PHONY: all clean fclean
