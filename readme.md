# Project: EasyEyes-openCV
### Created by Om Ambarkar
<br/>
<br/>

## **Working**: Separating the forground(Subject) from the background of the video and making the background negative to make the video less irritating to eyes.
<br/>

## Usage Reference
 

### function: processVideo()

```http
  calling the function processVideo()
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `inputVideo` | `string` | **Required**. This is the name of your target video |
| `outputVideo` | `string` | **Required**. This is the name of your processed video |
| `subjectThreshold` | `float` | **Required**. Its the threshold of the subject of your video |
| `backgroundThreshold` | `float` | **Required**. Its the threshold of the subject of your video |

<br/>

### Prerequisits Packages
```http
  pip3 install virtualenv
```

### Creating a virtual environment
```http
  virtualenv env
```

### Start the virtual environment
```http
  source env/bin/activate
```
<br/>

### Basic packages to be installed

| Package Names | Install     |
| :-------- | :------- |
| `cvzone` |   pip3 install cvzone |
| `mediapipe`|  pip3 install mediapipe |
| `moviepy` |  pip3 install moviepy |

