# MibiLogger
Create logs easier in Python 3 !

---

[TOC]

## Getting Started
Copy the folder named `MibiLogger` into the directory, and follow this [instructions](#Documentation) :

## Documentation
### `Mibilogger.debuglog`
`from MibiLogger.debuglog import *`
or
`import MibiLogger.debuglog`
#### `startlog(description=None)`

**Example** : 

```
from MibiLogger.debuglog import *

startlog("My description")
```

Will be display :

![Result](https://raw.githubusercontent.com/mibi88/MibiLogger/main/example_imgs/example1.png)

#### `errorlog(error_name, error_type, value)`

**Example** : 

```

from MibiLogger.debuglog import *

startlog("My description")
errorlog("Demo error","mibilogger_demo","Cool !")

```

Will be display :

![Result](https://raw.githubusercontent.com/mibi88/MibiLogger/main/example_imgs/example2_1.png)

#### `infolog(error_name, error_type, value)`

**Example** : 

```
from MibiLogger.debuglog import *

startlog("My description")
infolog("Demo info","mibilogger_demo","Cool !")
```

Will be display :

![Result](https://raw.githubusercontent.com/mibi88/MibiLogger/main/example_imgs/example3.png)

#### `warninglog(error_name, error_type, value)`

**Example** : 

```
from MibiLogger.debuglog import *

startlog("My description")
warninglog("Demo warning","mibilogger_demo","Cool !")
```

Will be display :

![Result](https://raw.githubusercontent.com/mibi88/MibiLogger/main/example_imgs/example4.png)
