/* SQLEditor (Postgres)*/

CREATE TABLE areas
(
id SERIAL NOT NULL UNIQUE ,
nombre VARCHAR(200) UNIQUE ,
CONSTRAINT "areas_pkey" PRIMARY KEY (id)
);

CREATE TABLE catalogo
(
id SERIAL NOT NULL UNIQUE ,
detalle VARCHAR(200),
CONSTRAINT "catalogo_pkey" PRIMARY KEY (id)
);

CREATE TABLE "detalle_catalogo"
(
id SERIAL NOT NULL UNIQUE ,
nombre VARCHAR(200),
"id_catalogo" INTEGER NOT NULL,
"id_relacion" INTEGER,
CONSTRAINT "detalle_catalogo_pkey" PRIMARY KEY (id)
);

CREATE TABLE ies
(
id SERIAL NOT NULL UNIQUE ,
acronimo CHARACTER(200) UNIQUE ,
nombre VARCHAR(200) UNIQUE ,
tipo VARCHAR(200),
categoria CHAR(2),
"sitio_web" VARCHAR(200) UNIQUE ,
"total_docentes" INTEGER,
"total_docentes_phd" INTEGER,
CONSTRAINT "ies_pkey" PRIMARY KEY (id)
);

CREATE TABLE extension
(
id SERIAL NOT NULL UNIQUE ,
"id_ies" INTEGER,
direccion VARCHAR(200),
telefono VARCHAR(200),
latitud VARCHAR(200),
longitud VARCHAR(200),
"id_ciudad" INTEGER,
CONSTRAINT "extension_pkey" PRIMARY KEY (id)
);

CREATE TABLE "ies_carreras"
(
id SERIAL NOT NULL UNIQUE ,
"id_carrera" INTEGER,
"id_ies" INTEGER,
CONSTRAINT "ies_carreras_pkey" PRIMARY KEY (id)
);

CREATE TABLE matriculados
(
id SERIAL NOT NULL UNIQUE ,
genero VARCHAR(10),
total INTEGER,
"id_ies" INTEGER,
CONSTRAINT "matriculados_pkey" PRIMARY KEY (id)
);

CREATE TABLE matriz
(
id SERIAL NOT NULL UNIQUE ,
"id_ies" INTEGER,
direccion VARCHAR(200),
telefono VARCHAR(200),
latitud VARCHAR(200),
longitud VARCHAR(200),
"id_ciudad" INTEGER,
CONSTRAINT "matriz_pkey" PRIMARY KEY (id)
);

CREATE TABLE modalidad
(
id SERIAL NOT NULL UNIQUE ,
nombre VARCHAR(200),
descripcion VARCHAR(200),
CONSTRAINT "modalidad_pkey" PRIMARY KEY (id)
);

CREATE TABLE "carreras_modalidad"
(
id SERIAL NOT NULL UNIQUE ,
"id_carrera" INTEGER,
"id_modalidad" INTEGER,
CONSTRAINT "carreras_modalidad_pkey" PRIMARY KEY (id)
);

CREATE TABLE "nivel_formacion"
(
id SERIAL NOT NULL UNIQUE ,
nivel VARCHAR(200),
CONSTRAINT "nivel_formacion_pkey" PRIMARY KEY (id)
);

CREATE TABLE carreras
(
id SERIAL NOT NULL UNIQUE ,
nombre VARCHAR(200) UNIQUE ,
"tipo_formacion" VARCHAR(200),
"id_area" INTEGER,
"id_nivel" INTEGER,
CONSTRAINT "carreras_pkey" PRIMARY KEY (id)
);

CREATE TABLE sede
(
id SERIAL NOT NULL UNIQUE ,
"id_ies" INTEGER,
direccion VARCHAR(200),
telefono VARCHAR(200),
latitud VARCHAR(200),
longitud VARCHAR(200),
"id_ciudad" INTEGER,
CONSTRAINT "sede_pkey" PRIMARY KEY (id)
);

CREATE TABLE titulados
(
id SERIAL NOT NULL UNIQUE ,
total INTEGER,
"id_nivel" INTEGER,
"id_pais" INTEGER,
CONSTRAINT "titulados_pkey" PRIMARY KEY (id)
);

ALTER TABLE "detalle_catalogo" ADD FOREIGN KEY ("id_catalogo") REFERENCES catalogo (id);

ALTER TABLE "detalle_catalogo" ADD FOREIGN KEY ("id_relacion") REFERENCES "detalle_catalogo" (id);

ALTER TABLE extension ADD FOREIGN KEY ("id_ies") REFERENCES ies (id);

ALTER TABLE extension ADD FOREIGN KEY ("id_ciudad") REFERENCES "detalle_catalogo" (id);

ALTER TABLE "ies_carreras" ADD FOREIGN KEY ("id_carrera") REFERENCES carreras (id);

ALTER TABLE "ies_carreras" ADD FOREIGN KEY ("id_ies") REFERENCES ies (id);

ALTER TABLE matriculados ADD FOREIGN KEY ("id_ies") REFERENCES ies (id);

ALTER TABLE matriz ADD FOREIGN KEY ("id_ies") REFERENCES ies (id);

ALTER TABLE matriz ADD FOREIGN KEY ("id_ciudad") REFERENCES "detalle_catalogo" (id);

ALTER TABLE "carreras_modalidad" ADD FOREIGN KEY ("id_carrera") REFERENCES carreras (id);

ALTER TABLE "carreras_modalidad" ADD FOREIGN KEY ("id_modalidad") REFERENCES modalidad (id);

ALTER TABLE carreras ADD FOREIGN KEY ("id_area") REFERENCES areas (id);

ALTER TABLE carreras ADD FOREIGN KEY ("id_nivel") REFERENCES "nivel_formacion" (id);

ALTER TABLE sede ADD FOREIGN KEY ("id_ies") REFERENCES ies (id);

ALTER TABLE sede ADD FOREIGN KEY ("id_ciudad") REFERENCES "detalle_catalogo" (id);

ALTER TABLE titulados ADD FOREIGN KEY ("id_nivel") REFERENCES "nivel_formacion" (id);

ALTER TABLE titulados ADD FOREIGN KEY ("id_pais") REFERENCES "detalle_catalogo" (id);
