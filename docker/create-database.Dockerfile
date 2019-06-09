FROM ubuntu:18.04

RUN apt -qyy update && apt -qyy upgrade
RUN apt -qyy install postgresql-client
