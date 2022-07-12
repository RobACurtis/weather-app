drop schema "public" cascade;

create schema "public";

CREATE TABLE "weatherforecast" (
  "id" serial NOT NULL,
  "date" TEXT NOT NULL,
	"timezone" TEXT NOT NULL,
	"lattitude" TEXT NOT NULL,
	"longitude" TEXT NOT NULL,
	"sunrise" TEXT NOT NULL,
	"sunset" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	"humidity" TEXT NOT NULL,
	"temperature-high" TEXT NOT NULL,
	"temperature-low" TEXT NOT NULL,
	CONSTRAINT "weather-forecast_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);
