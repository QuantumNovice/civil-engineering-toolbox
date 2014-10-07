import cherrypy
from controller.structure import steel_profile
from controller.geotechnic import surcharge_load
from controller.math import converter
from controller.about import about

def setup():
    #Router handler
    router = cherrypy.dispatch.RoutesDispatcher()

    #STRUCTURE
    a = steel_profile.Steel_Profile()
    router.connect(name='structure_steel_profile', route='/structure/steel-profile',
                   controller=a, action="index")
    #GEOTECHNIC
    a = surcharge_load.Surcharge_Load()
    router.connect(name='surcharge_point', route='/geotechnic/surcharge/point-load',
                   controller=a, action="point")
    router.connect(name='surcharge_point_img', route='/geotechnic/surcharge/point_image.png',
                   controller=a, action="point_image_png")
    router.connect(name='surcharge_strip', route='/geotechnic/surcharge/strip-load',
                   controller=a, action="strip")
    #MATH
    a = converter.Converter()
    router.connect(name='index_converter', route='/math/unit-converter',
                   controller=a, action="index")
    router.connect(name='distance_converter', route='/math/unit-converter/distance/',
                   controller=a, action="distance")
    router.connect(name='pressure_converter', route='/math/unit-converter/pressure/',
                   controller=a, action="pressure")
    router.connect(name='force_converter', route='/math/unit-converter/force/',
                   controller=a, action="force")
    #ABOUT
    a = about.About()
    router.connect(name='about', route='/about',
                   controller=a, action="index")
    router.connect(name='license', route='/about/license',
                   controller=a, action="license")
    router.connect(name='technology', route='/about/technology',
                   controller=a, action="technology")
    router.connect(name='home', route='/',
                   controller=a, action="home")
    router.connect(name='options', route='/options',
                   controller=a, action="options")
    router.connect(name='reset_options', route='/options/reset',
                   controller=a, action="reset_options")
    router.connect(name='set_options', route='/options/save',
                   controller=a, action="set_options")


    #Connect router handler as src
    router_config = {
        "/" : {
            "request.dispatch" : router
        }
    }
    return router_config
