import firebase from 'firebase/app';
import 'firebase/database';
const firebaseConfig = {
    apiKey: "AIzaSyDOOllUiySdUzRM9HbG2gbO1KuO0r5aw20",
    authDomain: "avida-724a9.firebaseapp.com",
    projectId: "avida-724a9",
    storageBucket: "avida-724a9.appspot.com",
    messagingSenderId: "401367208077",
    appId: "1:401367208077:web:0122642c1112a39d0d92c4",
    measurementId: "G-L3H7YC35VF"
  };

  firebase.initializeApp(firebaseConfig);

  // reference your database
  var avidaDB = firebase.database().ref("avida");
  
  document.getElementById("avida").addEventListener("submit", submitForm);
  
  function submitForm(e) {
    e.preventDefault();
  
    var name = getElementVal("name");
    var emailid = getElementVal("emailid");
    var msgContent = getElementVal("msgContent");
  
    saveMessages(name, emailid, msgContent);
  
    //   enable alert
    document.querySelector(".alert").style.display = "block";
  
    //   remove the alert
    setTimeout(() => {
      document.querySelector(".alert").style.display = "none";
    }, 3000);
  
    //   reset the form
    document.getElementById("avida").reset();
  }
  
  const saveMessages = (name, emailid, msgContent) => {
    var newavida = avidaDB.push();
  
    newavida.set({
      name: name,
      emailid: emailid,
      msgContent: msgContent,
    });
  };
  
  const getElementVal = (id) => {
    return document.getElementById(id).value;
  };
