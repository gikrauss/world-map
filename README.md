world-map - A world map generator
=============

## Setup ##

- Install requirements: pip install -r requirements.txt
- Sign Up for the Google Maps API: https://developers.google.com/maps/signup

## Running ##

```
$> API_KEY=<YOUR_KEY> python map.py
```

It's possible to run the application without an API key but the number of requests to Google Maps API without one are limited so you might run into problems rather quickly.

## Download PNG ##

The simplest way to generate a single PNG file is to use one of the many Chrome extensions that capture an entire web page.

I've used [Full Page Screen Capture](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl?utm_source=chrome-ntp-icon) successfully.

## Example ##

Scale down from 16565x9152px to 858x474px:

![world map](https://raw.github.com/gikrauss/world-map/master/examples/world-map.png)

Detailed section at 100%:

![world map detail](https://raw.github.com/gikrauss/world-map/master/examples/world-map-detail.png)
