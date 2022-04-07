function newLineIngredients() {
    num_of_rows = $('#ingredients').attr("rows");
    add_row = parseInt(num_of_rows) + 1;
    $("#ingredients").attr("rows", add_row);
}
function newLineInstructions() {
    num_of_rows = $('#instructions').attr("rows");
    add_row = parseInt(num_of_rows) + 1;
    $("#instructions").attr("rows", add_row);
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



