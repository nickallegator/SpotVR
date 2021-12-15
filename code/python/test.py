import bosdyn.client
from bosdyn.client.image import ImageClient
from PIL import Image
import io

sdk = bosdyn.client.create_standard_sdk('understanding-spot')

robot = sdk.create_robot('192.168.80.3')

id_client = robot.ensure_client('robot-id')

robot.authenticate('user2', 'simplepassword')

state_client = robot.ensure_client('robot-state')

image_client = robot.ensure_client(ImageClient.default_service_name)
sources = image_client.list_image_sources()

image_response = image_client.get_image_from_sources(["left_fisheye_image"])[0]
image = Image.open(io.BytesIO(image_response.shot.image.data))
image.show()