FROM trino:476

COPY --chown=root:trinogrp etc $TRINO_HOME/trino-server-476/etc

ENV PATH=$TRINO_HOME/trino-server-476/bin:$PATH

WORKDIR $TRINO_HOME/trino-server-476/bin

# COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT [ "launcher" ]
CMD ["run"]