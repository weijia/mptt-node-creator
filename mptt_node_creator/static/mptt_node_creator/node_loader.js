$(function() {
        var level = 1;

        function attach_magic_suggest(div_elem){
            var elem = $("input", div_elem);
            var ms = elem.magicSuggest({
                data: base_tree_url,
//                allowDuplicates: false,
                resultsField: "objects",
                valueField: "id",
                displayField: "content",
                method: "GET"
            });
            div_elem.attr("ms", ms);
            $(ms).on("selectionchange", function(e, control, selects){

                    console.log(ms);

                    if(selects.length == 0){
                        return;
                    }
                    var next_level = parseInt(div_elem.attr("level"))+1;
                    var next_level_div_elem = $("#level-"+next_level);
                    if(next_level_div_elem.length>0){
                        $("input", next_level_div_elem).focus();
                        return
                    };

                    var new_div_with_input = $('<div class="col-md-2" level="'+
                        next_level+'" id="level-'+next_level+'">'+
                            '<input class="form-inline"/>'+
                        '</div>');
                    $("#input-holder").append(new_div_with_input);
                    var new_ms = attach_magic_suggest(new_div_with_input);
//                    new_ms.focus();
                    var new_input = $("input", new_div_with_input)[0];
                    setTimeout(function(){
                        $(new_input).focus();
                        ms.collapse();
                    }, 50);

                    console.log(new_input);
//                    $(new_input).focus();
//                    $(new_input).select();
            });
//            $(ms).on("selectionchange", function(a, b){
//                console.log("another selectionchange");
//            });
            return ms;
        }
        attach_magic_suggest($("#level-0"));
    });