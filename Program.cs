using System;

// dotnet add package pythonnet
using Python.Runtime;
// python --version
Runtime.PythonDLL = "python311.dll";
PythonEngine.Initialize();

dynamic tf = Py.Import("tensorflow");
dynamic np = Py.Import("numpy");
dynamic model = tf.keras.models.load_model("checkpointSave/");

int index = 0;

// pip install pillow
dynamic list = new PyList();
list.append(tf.keras.utils.load_img("tests/"));

dynamic data = np.array(list);
dynamic result = model.predict(data);

Console.WriteLine(result[index]);
PythonEngine.Shutdown();
