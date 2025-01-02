#!/bin/bash

# Establece el número de página inicial
PAGE=1
PER_PAGE=100
HAS_MORE=true
PROPIETARY_NAME="Mario Cabrero Volarich as Cartago"
YEAR=$(date +%Y)

# Recorre todas las páginas de la API para obtener todos los repositorios
while $HAS_MORE; do
  # Solicita los repositorios de la página actual
  repos=$(curl -s -H "Authorization: token ${OWN_GITHUB_TOKEN}" \
    "https://api.github.com/user/repos?per_page=$PER_PAGE&page=$PAGE" | jq -r '.[].full_name')

  # Si la respuesta está vacía, significa que hemos llegado al final
  if [ -z "$repos" ]; then
    HAS_MORE=false
  else
    # Procesa cada repositorio
    for repo in $repos; do
      # Verifica si el directorio ya existe
      dir_name=$(basename $repo)
      if [ ! -d "$dir_name" ]; then
        # Clona el repositorio
        git clone https://github.com/$repo.git
        cd $dir_name


        # Verificar si el archivo LICENSE existe
        if [ ! -f LICENSE ]; then
          # Si no existe, lo creamos con la Licencia MIT
          echo "MIT License" > LICENSE
          echo "" >> LICENSE
          echo "Copyright (c) ${YEAR} ${PROPIETARY_NAME}" >> LICENSE
          echo "" >> LICENSE
          echo "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is provided to do so, subject to the following conditions:" >> LICENSE
          echo "" >> LICENSE
          echo "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software." >> LICENSE
          echo "" >> LICENSE
          echo "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE." >> LICENSE
          
          git add LICENSE
          git commit -m "Add MIT License"
          # Obtener la rama predeterminada
          default_branch=$(curl -s -H "Authorization: token ${OWN_GITHUB_TOKEN}" \
            "https://api.github.com/repos/${repo}" | jq -r '.default_branch')
          git push origin $default_branch
        fi
        cd ..
      else
        echo "Directory $dir_name already exists, skipping clone."
      fi
    done
  fi

  # Incrementa el número de página para la siguiente solicitud
  ((page++))
done
