select  distinct events.event_type,event_name,count(*) as counts
from events 
join event_identifier on events.event_type=event_identifier.event_type
group by events.event_type,event_name
order by events.event_type