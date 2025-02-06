# CEDA Sentinel Relay Hub tools

This codebase provides a set of tools to interact with the CEDA DHS series Data Hub Relay (DHR) based on the ESA/SERCO GSS implementation.
These tools will allow interaction with the GSS endpoint on the CEDA DHR and will allow programmatic control of such functions as Producers, Consumers and Ingesters.
The DHS GSS system is based upon a set of Docker Containers running within Docker Swarm and has the following components:

 - GSS-Ingest is the part of the system which connects to sources (CDSE, DHuS, other GSS, Swift container or directory) to get products and put them into the system (Datastores and Metadatastores)
 - GSS-Catalogue is the access point to products stored in the system. Users need to authenticate first and then access to data and metadata.
 - GSS-Admin is a REST API used to configure Ingesters, Datastores, DatastoreGroups, MetadataStores, Quotas and their properties.
 - GSS-Toolbox is a set of scripts to initialize the database and the index (Solr)
 - GSS-Notification notifies a defined end point on product deletion activity

The tools in this repository will interact with the GSS Admin API and provide users the ability to control the data flow from various sources and where this data is placed to allow CEDA full operational control of the GSS analogous to the previous system (DHuS) synchroniser setup.

These operations are grouped as such:

## List existing producer/consumers on local GSS.
This script shall list both matched producer and consumer pairs previously created and installed on the target GSS.  This script wraps a GET to the respective GSS API endpoints:

- http://<gss-admin-api>:8082/gss-admin-api/producers
- http://<gss-admin-api>:8082/gss-admin-api/consumers/

`list_producer_consumers -l local_gss_instance.cfg `

Where:  

`-l` is the option to define the hub (or otherwise) where the operation shall be submitted.  i.e. The local GSS instance we want to see the list of producers on.  
`-s` is an optional string filter to be supplied to match content returned according to original filter.  
`-t` is an optional string filter field defining the number of hours the LCD is behind the current date-time. If the `-e` option is used this will send output to the email address defined in the `-e` option. This will allow the user to identify where producer/consumer pairs are falling behind.  
`-e` is an optional string containing an email address to be sent a warning if the `-t` option is used. Can only be used if the `-t` option is used.  
`-f` is an option to output to stdout the detailed information associated with the given named producer or consumer i.e. "folder_producer1".  The script will render the full JSON returned in a human readable format.

The output from this should group the matched producers and consumers together with basic information on the associated source URL (source hub/GSS i.e. Colhub2), the GSS instance being used (i.e. srh-services13) , filter parameter and Last Creation Date (LCD) in tabular form.


## Create a new producer/consumer pair on the local GSS
This script shall allow users to generate a new producer/consumer pair on the target host based on the values within the files associated with the supplied options.  Other options shall be used to defined the search string and Last Creation date.  Other options may eventually be added to supplant/override other fields within the producer/consumer template.


`create_producer_consumer -t sentinel_2_producer.template -c colhub.cfg -l local_gss_instance.cfg`  


Where:  
`-t` is the option to define the template to be used to generate the JSON to POST to the defined instance (in the `-l` option)  i.e. The local GSS instance we want to see the list of producers on.  
`-c` is the option to provide the unencrypted credentials to be used in the POST-ed template to be used in the defined instance (in the `-l` option).  
`-l` is the option to define the hub (or otherwise) where the operation shall be submitted.  i.e. The local GSS instance we want to see the list of producers on.  
`-F` is used to supply a filter string i.e. startswith(Name,'S1')  
`-L` is used to define a LastPublicationDate i.e. 2025-01-15T00:00:00.00.  (Optional will use current date-time if not supplied).  



## Delete or remove producer/consumers
This script shall allow users to remove paired producer/consumers (previously identified in the list tool).  It shall use the DELETE operation.

`delete_producer_consumer -l local_gss_instance.cfg -n <producer_consumer base name`>

The script shall parse the HTTP response to report whether this operation was successful


## Adjust Quotas

## Adjust HFS Data stored

## 

