import React from 'react';
import './App.css';
import { IKContext, IKImage, IKUpload } from 'imagekitio-react';

const urlEndpoint = 'https://ik.imagekit.io/nd0pfd7urs99';
const publicKey = 'public_9ykx23W51aGNIyoclWqNMQhim/0=';
const authenticationEndpoint = 'http://localhost:3001/auth';

const onError = err => {
  console.log("Error", err);
}
const onSuccess = res => {
  console.log("Success", res);
}

function App() {
  return (
    <div className="App">
      <IKContext publicKey={publicKey} urlEndpoint={urlEndpoint} authenticationEndpoint={authenticationEndpoint}>
        <IKUpload
          onError={onError}
          onSuccess={onSuccess}
        />
        <IKImage path={InputEvent.fileName} width="400" />
      </IKContext>
    </div>
  );
}
export default App;
