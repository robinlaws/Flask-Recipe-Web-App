/* adds line to ingredients text area */
function newLineIngredients() {
    num_of_rows = $('#ingredients').attr("rows");
    add_row = parseInt(num_of_rows) + 1;
    $("#ingredients").attr("rows", add_row);
}

/* adds line to instructions text area */
function newLineInstructions() {
    num_of_rows = $('#instructions').attr("rows");
    add_row = parseInt(num_of_rows) + 1;
    $("#instructions").attr("rows", add_row);
}

/* shows recipe input when add recipe link is clicked */
function showAddRecipe(){
$("#add_recipe").toggle("container");
}

/*shoes delete recipe when link is clicked */
function showDelRecipe(){
$("#del_recipe").toggle("container");
}

/*shows review section when add review is clicked */
function showReviews() {
$("#reviews").toggle("container");
}

/* shoes usser reviews when link is clicked */
function showReviewed() {
$("#show_reviews").toggle("container");
}



