function deleteRecipe(recipeId) {
    fetch('/delete-recipe', {
        method: 'POST',
        body: JSON.stringify({recipeId: recipeId})
    }).then((_res) => {
    window.location.href = "/";
    });
    }

function newLineIngredients() {
    $('<input type="text" class="form-control" value="" name="ingredients">').insertAfter($("#ingredients"));
}
function newLineInstructions() {
    $('<input type="text" class="form-control" value="" name="instructions">').insertAfter($("#instructions"));
}
function delLineIngredients() {
   $("#ingredients").siblings(":last").remove();
}
function delLineInstructions(){
   $("#instructions").siblings(":last").remove();
}

function showAddRecipe(){
$("#add_recipe").toggle("container");
}
function showDelRecipe(){
$("#del_recipe").toggle("container");
}

function showReviews() {
$("#reviews").toggle("container");
}
function showReviewed() {
$("#show_reviews").toggle("container");
}


