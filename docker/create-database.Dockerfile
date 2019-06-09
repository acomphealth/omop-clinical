FROM ubuntu:18.04

RUN apt -qyy update && apt -qyy upgrade
RUN apt -qyy install postgresql-client

RUN mkdir /omop
WORKDIR /omop

COPY ddl/postgres/ /omop/

CMD psql -h host.docker.internal -U postgres -f omop_standard_ddl.sql && psql -h host.docker.internal -U postgres -f omop_standard_idx.sql && psql -h host.docker.internal -U postgres -f omop_standard_constraint.sql
