import sys
import torch
import os
import shutil
import subprocess
import re

python_version = sys.version
version_match = re.match(r"(\d+\.\d+)", python_version)

if version_match:
    python_version = version_match.group(1)
else:
    python_version = "N/A"
cuda_version = torch.version.cuda if torch.cuda.is_available() else "N/A"

cuda_bin_path = None
tensorrt_lib_path = None

if cuda_version != "N/A":
    cuda_major, cuda_minor = cuda_version.split('.')[:2]
    cuda_bin_path = fr"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v{cuda_major}.{cuda_minor}\bin"

current_directory = os.getcwd()
tensorrt_path = os.path.join(current_directory, "TensorRT")
if os.path.exists(tensorrt_path):
    tensorrt_lib_path = os.path.join(tensorrt_path, "lib")

with open('info.txt', 'w') as info_file:
    info_file.write(f"Versione di Python: {python_version}\n")
    info_file.write(f"Versione di cudatoolkit: {cuda_version}\n")
    if cuda_bin_path:
        info_file.write(f"Percorso delle librerie CUDA: {cuda_bin_path}\n")
    else:
        info_file.write("Devi installare cudatoolkit e cudnn prima di procedere\n")
    if tensorrt_lib_path:
        info_file.write(f"Percorso di TensorRT: {tensorrt_lib_path}\n")
        
        if cuda_bin_path:
            dll_files = [file for file in os.listdir(tensorrt_lib_path) if file.endswith(".dll")]
            for dll_file in dll_files:
                src_path = os.path.join(tensorrt_lib_path, dll_file)
                dst_path = os.path.join(cuda_bin_path, dll_file)
                shutil.copy(src_path, dst_path)
            info_file.write("Copiati i file DLL da TensorRT a CUDA bin directory\n")
        else:
            info_file.write("Non è stato possibile copiare i file DLL da TensorRT a CUDA bin directory perché CUDA non è disponibile\n")
        
        # Open the 'TensorRT' directory and look for the 'uff' subdirectory
        uff_directory = os.path.join(tensorrt_path, "uff")
        if os.path.exists(uff_directory):
            info_file.write("Percorso della cartella uff: {}\n".format(uff_directory))
            
            # Look for the '.whl' file inside the 'uff' directory
            whl_file = None
            for file in os.listdir(uff_directory):
                if file.endswith(".whl"):
                    whl_file = os.path.join(uff_directory, file)
                    break
            
            if whl_file:
                info_file.write("Percorso del file '.whl' nella cartella uff: {}\n".format(whl_file))
                try:
                    subprocess.run(["pip", "install", whl_file], check=True)
                    info_file.write("Installato il file 'uff.whl' con successo usando pip\n")
                except subprocess.CalledProcessError as e:
                    info_file.write("Errore nell'installazione del file 'uff.whl' con pip: {}\n".format(e))
            else:
                info_file.write("Nessun file '.whl' trovato nella cartella uff\n")
        else:
            info_file.write("La cartella 'uff' non è presente nella cartella TensorRT\n")
            
        # Open the 'TensorRT' directory and look for the 'onnx_graphsurgeon' subdirectory
        onnx_graphsurgeon_directory = os.path.join(tensorrt_path, "onnx_graphsurgeon")
        if os.path.exists(onnx_graphsurgeon_directory):
            info_file.write("Percorso della cartella onnx_graphsurgeon: {}\n".format(onnx_graphsurgeon_directory))
            
            # Look for the '.whl' file inside the 'onnx_graphsurgeon' directory
            onnx_graphsurgeon_whl = None
            for file in os.listdir(onnx_graphsurgeon_directory):
                if file.endswith(".whl"):
                    onnx_graphsurgeon_whl = os.path.join(onnx_graphsurgeon_directory, file)
                    break
            
            if onnx_graphsurgeon_whl:
                info_file.write("Percorso del file '.whl' nella cartella onnx_graphsurgeon: {}\n".format(onnx_graphsurgeon_whl))
                try:
                    subprocess.run(["pip", "install", onnx_graphsurgeon_whl], check=True)
                    info_file.write("Installato il file 'onnx_graphsurgeon.whl' con successo usando pip\n")
                except subprocess.CalledProcessError as e:
                    info_file.write("Errore nell'installazione del file 'onnx_graphsurgeon.whl' con pip: {}\n".format(e))
            else:
                info_file.write("Nessun file '.whl' trovato nella cartella onnx_graphsurgeon\n")
        else:
            info_file.write("La cartella 'onnx_graphsurgeon' non è presente nella cartella TensorRT\n")
            
        # Open the 'TensorRT' directory and look for the 'graphsurgeonn' subdirectory
        graphsurgeonn_directory = os.path.join(tensorrt_path, "graphsurgeon")
        if os.path.exists(graphsurgeonn_directory):
            info_file.write("Percorso della cartella graphsurgeon: {}\n".format(graphsurgeonn_directory))
            
            # Look for the '.whl' file inside the 'graphsurgeonn' directory
            graphsurgeon_whl = None
            for file in os.listdir(graphsurgeonn_directory):
                if file.endswith(".whl"):
                    graphsurgeon_whl = os.path.join(graphsurgeonn_directory, file)
                    break
            
            if graphsurgeon_whl:
                info_file.write("Percorso del file '.whl' nella cartella graphsurgeon: {}\n".format(graphsurgeon_whl))
                try:
                    subprocess.run(["pip", "install", graphsurgeon_whl], check=True)
                    info_file.write("Installato il file 'graphsurgeon.whl' con successo usando pip\n")
                except subprocess.CalledProcessError as e:
                    info_file.write("Errore nell'installazione del file 'graphsurgeon.whl' con pip: {}\n".format(e))
            else:
                info_file.write("Nessun file '.whl' trovato nella cartella graphsurgeon\n")
        else:
            info_file.write("La cartella 'graphsurgeonn' non è presente nella cartella TensorRT\n")
        
        # Open the 'TensorRT' directory and look for the 'python' subdirectory
        python_directory = os.path.join(tensorrt_path, "python")
        if os.path.exists(python_directory):
            info_file.write("Percorso della cartella python: {}\n".format(python_directory))
            
            # Look for the '.whl' file inside the 'python' directory
            tensorrt_whl = None
            for file in os.listdir(python_directory):
                if file.startswith("tensorrt") and file.endswith(".whl"):
                    tensorrt_whl = os.path.join(python_directory, file)
                    break
            
            if tensorrt_whl:
                info_file.write("Percorso del file '.whl' nella cartella python: {}\n".format(tensorrt_whl))
                try:
                    subprocess.run(["pip", "install", tensorrt_whl], check=True)
                    info_file.write("Installato il file 'tensorrt.whl' con successo usando pip\n")
                except subprocess.CalledProcessError as e:
                    info_file.write("Errore nell'installazione del file 'tensorrt.whl' con pip: {}\n".format(e))
            else:
                info_file.write("Nessun file '.whl' trovato nella cartella python\n")
        else:
            info_file.write("La cartella 'python' non è presente nella cartella TensorRT\n")
    else:
        info_file.write("Devi scaricare la cartella di TensorRT dal sito NVIDIA e posizionarla dove si trova questo codice. PS: La cartella deve essere rinominata 'TensorRT' altrimenti non verrà trovata.\n")
