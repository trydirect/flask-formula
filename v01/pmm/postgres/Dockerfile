FROM postgres:latest


ENV GPG_KEYS \
# pub   1024D/CD2EFD2A 2009-12-15
#       Key fingerprint = 430B DF5C 56E7 C94E 848E  E60C 1C4C BDCD CD2E FD2A
# uid                  Percona MySQL Development Team <mysql-dev@percona.com>
# sub   2048g/2D607DAF 2009-12-15
	430BDF5C56E7C94E848EE60C1C4CBDCDCD2EFD2A \
# pub   4096R/8507EFA5 2016-06-30
#       Key fingerprint = 4D1B B29D 63D9 8E42 2B21  13B1 9334 A25F 8507 EFA5
# uid                  Percona MySQL Development Team (Packaging key) <mysql-dev@percona.com>
# sub   4096R/4CAC6D72 2016-06-30
	4D1BB29D63D98E422B2113B19334A25F8507EFA5
	
RUN set -ex; \
    	apt-get update; \
	apt-get install -y gnupg apt-transport-https; \
	export GNUPGHOME="$(mktemp -d)"; \
	for key in $GPG_KEYS; do \
                gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
                gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done; \
	gpg --export $GPG_KEYS > /etc/apt/trusted.gpg.d/percona.gpg; \
	rm -r "$GNUPGHOME"; \
	apt-key list; \
	echo 'deb https://repo.percona.com/apt stretch main' > /etc/apt/sources.list.d/percona.list; \
	apt-get update && apt-get install -y pmm-client; \
	apt-get remove --purge -y gnupg apt-transport-https; \
	apt-get autoremove -y --purge; \
	rm -rf /var/lib/apt/lists/* \
	true

COPY init.sql /docker-entrypoint-initdb.d/
COPY initpmm.sh /root/
