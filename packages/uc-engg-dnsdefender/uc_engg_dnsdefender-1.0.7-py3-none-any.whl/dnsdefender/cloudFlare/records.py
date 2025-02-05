from cloudflare import Cloudflare

def get_cloudflare_records(cloudflare_api_email,cloudflare_api_key, zones_to_check):
   cf = Cloudflare(api_email=cloudflare_api_email, api_key=cloudflare_api_key)
   dns_records = []
   all_zones = []

   page_number = 1
   while True:
       zones = cf.zones.list(per_page=100, page=page_number)
       if not zones.result:
           break

       for zone in zones:
           if not zones_to_check or zone.name in zones_to_check:
               all_zones.append(zone)

       page_number += 1

   print(f"Found {len(all_zones)} zones to process")

   for zone in all_zones:
       dns_page = 1
       while True:
           try:
               records = cf.dns.records.list(zone_id=zone.id, per_page=100, page=dns_page)
               if not records.result:
                   break

               for record in records:
                   if record.content:
                       dns_records.append({
                           "type": record.type,
                           "name": record.name,
                           "records": [record.content],
                           "source": "cloudflare",
                           "zone_name": zone.name
                       })

               dns_page += 1

           except Exception as e:
               print(f"Failed to retrieve DNS records for {zone.name}: {e}")
               break

   return dns_records