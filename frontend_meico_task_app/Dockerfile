FROM node:20.19.4-alpine

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos package.json y package-lock.json
COPY package*.json ./

# Instalamos dependencias
RUN npm install

# Copiamos todo el código
COPY . .

# Exponemos el puerto de Angular
EXPOSE 4200

# Comando por defecto: iniciar Angular en modo dev
CMD ["npm", "start"]
