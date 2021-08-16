var firebaseConfig = {
    apiKey: "AIzaSyAjc-Ekb_17oyxjHc4pR2s-CVK6Ncz-dYA",
    authDomain: "abcsdd-e95cf.firebaseapp.com",
    projectId: "abcsdd-e95cf",
    storageBucket: "abcsdd-e95cf.appspot.com",
    messagingSenderId: "47387944972",
    appId: "1:47387944972:web:23fc4864f225d6d4b2e629",
    measurementId: "G-F7D0F1X31R"
  };
firebase.initializeApp(firebaseConfig);
firebase.analytics();
const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
    didOpen: (toast) => {
        toast.addEventListener('mouseenter', Swal.stopTimer)
        toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
})


onAppInit()

var _user;
const redirect_to = "/home/"

function onAppInit() {
    firebase.auth().onAuthStateChanged((user) => {
        if(!user) return
        _user = user;
        const path=window.location.pathname;
        if (!user.emailVerified && path != '/verify/') {
            window.open("/verify/", "_self")
        }

        if (user.emailVerified && ["/login/","/create/","/verify/","/login","/create","/verify"].includes(path)) {
            createSession()
        }
        document.getElementById("span_email").innerText = user.email
    })
}

function createAccoutWithEmail() {
    let email = document.getElementById("email").value
    let password = document.getElementById("pass").value
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((user) => {
            sendVerificationLink(user)
           
        })
        .catch(err => catchBlockHandler(err))
}
function loginWithEmail() {
    let email = document.getElementById("email").value
    let password = document.getElementById("pass").value
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((userCredential) => {
            var user = userCredential.user;
            console.log(user);
        }).catch(err => catchBlockHandler(err))
}


function loginWithGoogle() {
    const googleAuthProvider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(googleAuthProvider).then(data => {
        console.log(data)
    }).catch(err => catchBlockHandler(err))
}

function loginWithFacebook() {
    var provider = new firebase.auth.FacebookAuthProvider();
    firebase.auth().signInWithPopup(provider).then(data => {
        console.log(data)
    }).catch(err => catchBlockHandler(err))
}

function sendVerificationLink(user = _user) {
    user.sendEmailVerification().then(() => {
        Toast.fire({
            icon: 'info',
            title: "Verification link has been sent"
        })
    }).catch(err => catchBlockHandler(err))
}


function forgetPassword(){
    Swal.fire({
        title: 'Enter Your Email',
        input: 'text',
        showCancelButton: true,
        confirmButtonText: 'Reset Password',
        showLoaderOnConfirm: true,
        preConfirm: (email) => {
            return firebase.auth().sendPasswordResetEmail(email)
        },
        allowOutsideClick: () => !Swal.isLoading()
      }).then((result) => {
        Toast.fire({
            icon: 'info',
            title: "Reset link has been sent to your email address"
        })
      }).catch(error=>catchBlockHandler(error))
}


function logout() {
    firebase.auth().signOut().then(() => {
        window.open("/login/", "_self")
    }).catch((error) => catchBlockHandler(error));
}

function catchBlockHandler(error) {
    var errorCode = error.code;
    var errorMessage = error.message;
    Toast.fire({
        icon: 'error',
        title: errorMessage
    })
}

function createSession() {
    firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then((idToken) => {
        console.log(idToken)
        fetch('/create_session', {
            method: 'GET',
            headers: {
                'Authorization': idToken
            },
        }).then(response=>{
            window.open(redirect_to, "_self")
            console.log(response)
        })
    }).catch((error) => {
        window.open(redirect_to, "_self")
        catchBlockHandler(error)
    });
}