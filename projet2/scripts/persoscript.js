//On initialise des variables compteurs qui vont stocker le nombre de réponses correspondant au profil
var nevro=0;
var psycho=0;
var socio=0;



//Fonction qui sera exécutée lors du clic sur le bouton valider du formulaire
function valider() {
	//On commence par récupérer la valeur du menu déroulant qui a été selectionner par l'utilisateur 
	 var perso = document.getElementById("perso");
   	 var perso_choisi = perso.options[perso.selectedIndex].value;

	}
	
	// Ensuite on ajoute la valeur dans la variable correspondante 

	if(perso_choisi=="n")
	{
		nevro=nevro+1;
	}
	else if(perso_choisi=="p")
	{
		psycho=psycho+1;
	}
	else
	{
		socio=socio+1;
	}
	
	
	//On regroupe les différents profils dans un tableau 
	var valeurs=[nevro,psycho,socio];
	var profils=["tu es névropathe","tu es psychopathe","tu es sociopathe"];
	
	//On cherche le maximum du tableau et son indice
	var max = valeurs[0];
    var indice_du_max = 0;
    
    for (var i = 1; i < valeurs.length; i++) {
        if (valeurs[i] > max) {
            indice_du_max = i;
            max = valeurs[i];
        }
    }
	
	//on affiche le profil qui a eu le maximum de réponses dans la balise à l'identifiant resultat
	document.getElementById("resultat").innerHTML= "la sentence est tombée :"+ profils[indice_du_max];
}


function test() {
	document.getElementById("teste").innerHTML= "sans blague"

  }

