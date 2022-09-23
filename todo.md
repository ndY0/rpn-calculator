## discussion autour de la structure du projet

le projet a une structure très simple, avec 3 services. un service expose une api pour l'objet de stack, les deux second sont liés à l'initialisation, le management et l'accès aux bases de donnée

en piste d'amélioration, il faudrait découpler la dépendance forte entre la couche d'accès à la base et les services en utilisant un orm (par exemple sqlalchemy). ce n'a pas été fait en raison du temps disponible

## pistes d'amélioration

- ajouter des TU
- revoir l'initialisation de l'application