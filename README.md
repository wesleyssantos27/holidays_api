# Calendarific API
Consuming data from the "calendarific" API. It is used to get holidays from different countries and regions.

Here is the API docs: https://calendarific.com/api-documentation


### Observed improvement points
When I tried to consume the API using client libraries I notice that python version used was 2.0. Althought there is one method used for dictionarys that no longer exists in version 3.0. 
The method "dict.has_key" can be changed for "key in dict". This second one exists in both python versions 2.0 and 3.0.
