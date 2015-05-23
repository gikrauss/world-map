from flask import Flask, render_template
app = Flask(__name__)
app.config.from_envvar('SETTINGS')

@app.route('/')
def map():
  zoom = 6
  latitudes = list(drange(-80, 80, 13.25))
  latitudes.reverse()
  latitudes = [67.875, 62.25, 55.35, 47.025, 37.16, 25.79, 13.25, 0, -13.25, -25.79, -37.16, -47.025, -55.35, -62.25, -67.875]
  #latitudes = [67.875, 62.25]
  longitudes = list(drange(-173, 180, 14))
  #longitudes = [163, 177]
  return render_template('map.html', latitudes=latitudes, longitudes=longitudes, zoom=zoom) 


def drange(start, stop, step):
  r = start
  while (r < stop):
  	yield r
  	r += step


if __name__ == '__main__':
  app.run(debug=True)

