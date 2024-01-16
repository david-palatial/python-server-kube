from concurrent import futures
import logging
import math
import time
import os
import unreal
import subprocess
import urllib.request
from pymongo import MongoClient
import sys
import urllib.request
import shutil
import boto3
import zipfile

import grpc
import PalatialWeb_pb2
import PalatialWeb_pb2_grpc
import glob

from pathlib import Path

import requests
import string
import random
import json
import paramiko

class importFunctions:
    # Define the paths
    project_path = unreal.Paths.project_dir()
    import_folder = os.path.join(unreal.Paths.project_dir(), 'import')
    assets_import_folder = "/Game/User/Import"


    def loadLevel(self):
        # Check if the 'import' level exists, otherwise create it
        level_path = "/Game/User/Main"
        level_system = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
        if not level_system.load_level(level_path):
            level_system.new_level(level_path)



    def importFiles(self):  

        link = sys.argv[2]

        current_working_directory = os.getcwd()

        file_name = current_working_directory + "/import/" + link.split("/")[-1]

        print("checking: " + self.import_folder)

        #ds_files = [f for f in glob_path.rglob("**/*.udatasmith")]
        glob_path = Path(self.import_folder)
        file_list = [f for f in glob_path.rglob("**/*.udatasmith")]
        for f in file_list:
            print(f)


        # Get a list of all Datasmith files in the import folder
        ds_files = [f for f in os.listdir(self.import_folder) if f.endswith('.udatasmith')]
        eas = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        ic_mng = unreal.InterchangeManager.get_interchange_manager_scripted()
        #pipeline = eas.load_asset("/Game/Palatial/Features/Dataprep/Recipes/DA_RevitPipeline")
        #mesh_pipeline = pipeline.get_editor_property("mesh_pipeline")
        dataprep_asset = unreal.EditorAssetLibrary.load_asset("/Game/Palatial/Features/Dataprep/Recipes/DA_RevitPipeline")
        dataprep_lib = unreal.EditorDataprepAssetLibrary()

        for ds_file in ds_files:
            dataprep_lib = unreal.EditorDataprepAssetLibrary()

            asset_path = self.project_path + "/Palatial/Features/Dataprep/Recipes/DA_RevitPipeline"
            if not dataprep_lib.get_producers_count(dataprep_asset): # or (isinstance(dataprep_lib.get_producer(dataprep_asset, 0), unreal.DatasmithDirProducer) and dataprep_lib.get_producer(dataprep_asset, 0).folder_path == import_folder):
                producer = dataprep_lib.add_producer_automated(dataprep_asset, unreal.DatasmithFileProducer)
                print(self.import_folder + ds_file)
                producer.set_editor_property("file_path" , self.import_folder + "/" + ds_file)
            else:
                if type(dataprep_lib.get_producer(dataprep_asset, 0)) is unreal.DatasmithFileProducer:
                    producer = dataprep_lib.get_producer(dataprep_asset, 0)
                    producer.set_editor_property("file_path" , self.import_folder + "/" + ds_file)
                else:
                    dataprep_lib.remove_producer(dataprep_asset, 0)
                    producer = dataprep_lib.add_producer_automated(dataprep_asset, unreal.DatasmithFileProducer)
                    print(self.import_folder + ds_file)
                    producer.set_editor_property("file_path" , self.import_folder + "/" + ds_file)


            consumer = dataprep_lib.get_consumer(dataprep_asset)
            consumer.set_level_name_automated(ds_file.split('.')[0])


            dataprep_asset = unreal.EditorAssetLibrary.load_asset("/Game/Palatial/Features/Dataprep/Recipes/DA_RevitPipeline")
            dataprep_lib.execute_dataprep(dataprep_asset, unreal.DataprepReportMethod.STANDARD_LOG, unreal.DataprepReportMethod.STANDARD_LOG)
            
            print("set producer to file: " + ds_file)

        # Import the Datasmith files into the level
        dataprep_lib.execute_dataprep(dataprep_asset, unreal.DataprepReportMethod.STANDARD_LOG, unreal.DataprepReportMethod.STANDARD_LOG)

    #   for ds_file in ds_files:
    #       ds_path = os.path.join(import_folder, ds_file)

    #       # Set import options
    #       options = unreal.DatasmithImportOptions()
    #       options.base_options.scene_handling = unreal.DatasmithImportScene.CURRENT_LEVEL
    #       options.base_options.include_geometry = True
    #       options.base_options.include_material = True
    #       options.base_options.include_light = True
    #       options.base_options.include_camera = True
    #       options.base_options.include_animation = True

    #       # Create the factory and set the options
    #       factory = unreal.DatasmithImportFactory()
    #       #factory.set_editor_property('import_options', options)

    #       # Import the Datapith file
    #       task = unreal.AssetImportTask()
    #       task.set_editor_property('filename', ds_path)
    #       task.set_editor_property('destination_path', assets_import_folder)
    #       task.set_editor_property('replace_existing', True)
    #       task.set_editor_property('save', True)
    #       task.set_editor_property('automated', True)
    #       task.set_editor_property('factory', factory)

    #       unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])



            

    def deleteFiles(self):
        # Get a list of all Datasmith files in the import folder
        ds_files = [f for f in os.listdir(self.import_folder) if f.endswith('.udatasmith')]


        for ds_file in ds_files:
            # Delete the Datasmith file from the import folder
            ds_path = os.path.join(self.import_folder, ds_file)
            os.remove(ds_path)

        print("Datasmith files imported and original files deleted from the 'import' folder.")

def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def execute_ssh_command(command):
  hostname = "palatial.tenant-palatial-platform.coreweave.cloud"
  port = 22
  username = "david"
  private_key_path = r"C:\Users\david\.ssh\id_rsa"

  client = paramiko.SSHClient()
  client.load_system_host_keys()

  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  try:
    client.connect(hostname, port, username, key_filename=private_key_path)
    stdin, stdout, stderr = client.exec_command(command)
    if stderr.channel.recv_exit_status() != 0:
      raise Execption(f"Failure executing the remote script: {stderr.read().decode()}")
    return stdout.read().decode()
  except Execption as e:
    print(f"Error: {str(e)}")
    return None
  finally:
    client.close()

class PalatialBuildServer:
    buildClientCommand = ""


    buildServerCommand = ""

    editActionQueue = []

    def __init__(self):
        print("build system initialized")

    def buildProject(self):
        os.system(self.buildClientCommand)

        #os.system(self.buildServerCommand)
        print("the packaging would start now")
        unreal.ImportEditorScriptLibrary.save_level()
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
        os.chdir(unreal.Paths.project_dir())
        print("test 1")
        
        batch_file_path = unreal.Paths.root_dir() + "Engine/Build/BatchFiles/RunUAT.bat "
        print("File Path : " + batch_file_path)
        command = 'BuildCookRun'
        project_path = r"C:\Users\david\Palatial_V01_UE53\Palatial_V01_UE53.uproject"
        output_directory = "."

        # Prepare the command with arguments
        arguments = [
            batch_file_path,
            'BuildCookRun',
            f'-project="{project_path}"',
            '-noP4',
            '-platform=Linux',
            '-clientconfig=Development',
            '-serverconfig=Development',
            '-cook',
            '-allmaps',
            '-build',
            '-stage',
            '-pak',
            '-archive',
            f'-archivedirectory="{output_directory}"'
        ]
        
        # Execute the command
        subprocess.call(arguments)
        print("test 2")
        
        workspace_name = "test"
        app_name = generate_random_string()

        print("deploying")
        Deploy = r'C:\Users\david\PythonServer\Deploy.bat'
        process = subprocess.Popen(f'{Deploy} {app_name}')
        process.wait()

        print("creating link")
        CreateLink = r'C:\Users\david\PythonServer\CreateLink.bat'
        stdout = execute_ssh_command(f'sudo -E python3 ~/link-deployment/run_pipeline https://{workspace_name}.palatialxr.com/{app_name} -C')

        app_payload = json.loads(stdout)

        print("getting components")
        response = requests.post("https://api.palatialxr.com/v1/k8s-components", json={"name": app_name}).json()


        updateChangelogs({
          "event": "import complete",
          "application": app_name,
          "url": app_payload["url"],
          "podComponents": response["data"]
        })



    def CommitEdits(self):
        valid_actions = self.process_undo_actions()
        print("Num actions after undo = " + str(len(valid_actions)) + " ," + 
              str(len(self.editActionQueue) - len(valid_actions)) + " undo actions proccessed")

        unreal.ImportEditorScriptLibrary.initialize_maps()
        
        for action in valid_actions:
            if isinstance(action, PalatialWeb_pb2.EditingAction):
                action_type = action.WhichOneof("edit_action")
                
                if action_type == "batch_delete_action":
                    mesh_ids = [delete.mesh_id for delete in action.batch_delete_action.delete_action]
                    unreal.ImportEditorScriptLibrary.batch_delete(mesh_ids)
                elif action_type == "batch_translate_action":
                    mesh_ids = []
                    mesh_locations = []

                    for translate in action.batch_translate_action.translate:
                        mesh_ids.append(translate.mesh_id)
                        mesh_locations.append(unreal.Vector(translate.location.x, translate.location.y, translate.location.z))
                        
                    unreal.ImportEditorScriptLibrary.batch_translate(mesh_ids, mesh_locations)
                elif action_type == "flip_normal_action":
                    unreal.ImportEditorScriptLibrary.flip_normal(action.flip_normal_action.mesh_id)
                elif action_type == "batch_light_setting_action":
                    for light_setting in action.batch_light_setting_action.light_setting_action:      
                        unreal.ImportEditorScriptLibrary.batch_light_settings(
                            light_setting.light_id,
                            light_setting.source_radius,
                            light_setting.soft_source_radius,
                            light_setting.source_length,
                            light_setting.inner_cone_angle,
                            light_setting.outer_cone_angle,
                            light_setting.source_width,
                            light_setting.source_weight,
                            light_setting.barn_door_angle,
                            light_setting.barn_door_length,
                            light_setting.intensity,
                            light_setting.attenuation,
                            unreal.LinearColor(light_setting.color_r, light_setting.color_g, light_setting.color_b),
                            light_setting.cast_shadows,
                            light_setting.enabled
                        )
                elif action_type == "add_light_action":
                    add_light = action.add_light_action
                    print("Add Light Action")
                    unreal.ImportEditorScriptLibrary.add_light(
                        add_light.unique_id,
                        add_light.type,
                        unreal.Vector(
                            add_light.location.x,
                            add_light.location.y,
                            add_light.location.z)
                    )
                elif action_type == "batch_replace_material_action":
                    mesh_ids = [id for id in action.batch_replace_material_action.mesh_ids]

                    unreal.ImportEditorScriptLibrary.batch_replace_material(
                        action.batch_replace_material_action.old_material_path,
                        action.batch_replace_material_action.new_material_path,
                        mesh_ids
                    )
                elif action_type == "toggle_nanite_action":
                    continue
                elif action_type == "adjust_context_action":
                    adjust_context = action.adjust_context_action

                    unreal.ImportEditorScriptLibrary.adjust_context(
                        adjust_context.long,
                        adjust_context.lat,
                        adjust_context.height,
                        adjust_context.angle
                    )
                elif action_type == "crop_context_action":
                    spline_points = [unreal.Vector(point.x, point.y, point.z) for point in action.crop_context_action.spline_point]
                    unreal.ImportEditorScriptLibrary.crop_context(spline_points)
                elif action_type == "place_context_action":
                    unreal.ImportEditorScriptLibrary.place_context(action.place_context_action.enabled)
                elif action_type == "set_saved_view_action":
                    set_saved_view = action.set_saved_view_action
                    print("Set Saved View")

                    unreal.ImportEditorScriptLibrary.set_saved_view(
                        set_saved_view.camera_id,
                        set_saved_view.enabled,
                        set_saved_view.name

                    )
                elif action_type == "add_saved_view_action":
                    add_saved_view = action.add_saved_view_action

                    unreal.ImportEditorScriptLibrary.add_saved_view(
                        add_saved_view.unique_id,
                        add_saved_view.name,
                        unreal.Vector(add_saved_view.location.x, add_saved_view.location.y, add_saved_view.location.z),
                        unreal.Vector(add_saved_view.rotation_x, add_saved_view.rotation_y, add_saved_view.rotation_z)
                    )
                elif action_type == "set_player_start_action":
                    unreal.ImportEditorScriptLibrary.set_player_start(action.set_player_start_action.camera_id)
                    print("Set Player Starter")
                else:
                    print(f"Unknown action_type: {action_type}")

    def process_undo_actions(self):
        valid_actions = []
        undo_count = 0

        for edit in reversed(self.editActionQueue):
            if isinstance(edit, PalatialWeb_pb2.EditingAction):
                action_type = edit.WhichOneof("edit_action")

                if action_type == "undo_action":
                    undo_count += 1
                elif undo_count > 0:
                    undo_count -= 1
                else:
                    valid_actions.append(edit)
        return list(reversed(valid_actions))

buildServer = PalatialBuildServer()
class PalatialWebServicer(PalatialWeb_pb2_grpc.PalatialServerServicer):


    def __init__(self, server):
        self.server = server
        print("grpc server initialized")

    def SendEditingCommand(self, request, context):
        print(request.WhichOneof("edit_action"))
        buildServer.editActionQueue.append(request)

        return PalatialWeb_pb2.Ack(ack = True)

    def CommitEdits(self, request, context):
        self.server.stop(1)
        print("stopped server")
        

        return PalatialWeb_pb2.Ack(ack = True)


def serve():
    
    cwd = os.getcwd()
    # Printing the current working directory
    print("The Current working directory is: {0}".format(cwd))
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    PalatialWeb_pb2_grpc.add_PalatialServerServicer_to_server(
        PalatialWebServicer(server), server)
    server.add_insecure_port('[::]:50051')
    print("starting GRPC server")
    server.start()
    server.wait_for_termination()

    buildServer.CommitEdits()

    buildServer.buildProject()

project_id = ""

def logIP():
    ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    print('My public IP address is: {}'.format(ip))

    print(project_id + " : " + ip)

    db = getMongoDB("palatial")
    server_map = db["server_map"]

    server_map.find_one_and_update({'project_id' : project_id}, {'$set': {'ip' : ip}}, upsert=True )
    print("added project map")



def getMongoDB(collection):
    
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient("mongodb://palatial:0UDUiKxwj7fI0@mongodb.mithyalabs.com:27017/palatial?directConnection=true&authSource=staging_db")
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client[collection]

def updateChangelogs(message):
    from bson import ObjectId
    import datetime
    current_datetime = datetime.datetime.now()
    db = getMongoDB("palatial")
    changelogs = db["changelogs"]

    payload = {
      "subjectId": ObjectId(project_id),
      "subjectType": "projects",
      "createdAt": current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    }
    payload.update(message)
    changelogs.insert_one(payload)

def downloadFiles(url):
    #url = "https://abad4791da6f642b2de41deee689ccaa.r2.cloudflarestorage.com/palatial-dev/uploads/projects/6564ebe00b14c666e6930bc8/"
    r2_url = url.split("/palatial-dev/", 1)[0]
    s3 = boto3.resource('s3',
    endpoint_url = r2_url,
    aws_access_key_id = 'f0a8fe7fd04f7f61824414cffc3249da',
    aws_secret_access_key = 'b04b7a50186aebaafb0e148a9ce2a0bae293d8d602831a44ab79974ef970a6dc'
    )

    save_location = os.path.join(unreal.Paths.project_dir(), 'import/')
    Path(save_location).mkdir(parents=True, exist_ok=True)

    os.chdir(save_location)
    palatial = s3.Bucket("palatial-dev")
    project = ""

    key = url.split("/palatial-dev/", 1)[1]
    objs = list(palatial.objects.filter(Prefix=key))

    for obj in objs:
        #print(obj.key)

        # remove the file name from the object key
        obj_path = os.path.dirname(obj.key)
        print(obj_path)
        #folder = obj_path.split("/")[-1]
        #obj_path = os.path.join(save_location, folder)
        obj_path = Path(save_location)
        print(obj_path)

        # create nested directory structure
        #Path(obj_path).mkdir(parents=True, exist_ok=True)

        local_file_path = os.path.join(obj_path, os.path.basename(obj.key))

        # save file with full path locally
        palatial.download_file(obj.key, local_file_path)
        if local_file_path.endswith(".zip"):
            zip_ref = zipfile.ZipFile(local_file_path)
            zip_ref.extractall(obj_path) # extract file to dir
            zip_ref.close() # close file
            os.remove(local_file_path) # delete zipped file
    
    glob_path = Path(save_location)
    print("Path: ", glob_path)

    file_list = [f for f in glob_path.rglob("**/*.udatasmith")]
    for f in file_list:
        print(f)


def checkProjectFolder():
    return


def makeProjectCopy():
    return


def setProjectFolder():
    return

#call this with 
if __name__ == '__main__':
    logging.basicConfig()

    os.chdir(r"C:\Users\david\Palatial_V01_UE53")

    url = ""
    if len(sys.argv) != 3:
        print("BuildServer argument mismatch detected. Falling back to matching mode.")
        if len(sys.argv) < 2:
            print("ERROR: No arguments detected. Shutting down.")
            sys.exit()
        checkVariable = sys.argv[1]
        if "https://" in checkVariable:
            print("Link detected.")
            url = checkVariable
            if len(checkVariable.split("/")[-1]) < 2:
                project_id = checkVariable.split("/")[-2]
            else:
                project_id = checkVariable.split("/")[-1]
        else:
            print("Project ID detected")
            project_id = checkVariable
            url = "https://abad4791da6f642b2de41deee689ccaa.r2.cloudflarestorage.com/palatial-dev/uploads/projects/" + project_id + "/"
    else:
        project_id = sys.argv[1]
        print("argv[1] : " + project_id)
        print("argv[2] : " + sys.argv[2])
        url = sys.argv[2]

    print("project_id : " + project_id)
    print("url : " + url)

    directory = os.path.join(unreal.Paths.project_dir(), 'import')
    cwd = os.getcwd()
    engine = unreal.Paths.engine_dir()
    # Printing the current working directory
    print("The Current working directory is: {0}".format(cwd))
    print("Download directory is: {0}".format(directory))
    print("Engine directory is: {0}".format(engine))

 
    updateChangelogs({ "event": "processing import" })

    downloadFiles(url)



    logIP()
    importInstance = importFunctions()
    importInstance.loadLevel()

    importInstance.importFiles()

    importInstance.deleteFiles()
    unreal.EditorLevelLibrary.save_all_dirty_levels()

    unreal.PalatialEditorFunctionLibrary.execute_post_import_scripts()
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)

    buildServer.buildProject()
    print("whoo got to the end without crashing!")
    while True:
        serve()

