FROM node:19-alpine   
#image environment blueprint: install node

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

COPY package.json /app/
COPY src /app/

WORKDIR  /app
# set the working directory. Same like: "cd ..."

RUN npm install 

CMD ["node", "server.js"]


#run docker build -t node-app:1.0 .  (to build)

# docker images (to check)