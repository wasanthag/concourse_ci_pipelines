FROM whewawal/cci-demo

COPY api.py /opt/
COPY templates /opt/templates
EXPOSE 5000
CMD python /opt/api.py

