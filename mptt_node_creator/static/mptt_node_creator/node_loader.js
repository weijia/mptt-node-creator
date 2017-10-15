$(function() {
        function attach_magic_suggest(div_elem, parent){
            var elem = $("input", div_elem);
            var additionalParam = {"parent": "None"};
            if(parent){
                additionalParam = {"parent": parent};
            }
            var ms = elem.magicSuggest({
                data: base_tree_url,
                resultsField: "objects",
                valueField: "id",
                displayField: "content",
                dataUrlParams: additionalParam,
                method: "GET"
            });
//            div_elem.attr("ms", ms);
            $(ms).on("selectionchange", function(e, control, selects){
                    console.log(ms);
                    if(selects.length == 0){
                        return;
                    }
                    var next_level = parseInt(div_elem.attr("level"))+1;
                    var next_level_div_elem = $("#level-"+next_level);
                    if(next_level_div_elem.length>0){
                        setTimeout(function(){
                            console.log("focus on", $("input", next_level_div_elem));
                            $("input", next_level_div_elem).focus();
                        }, 50);
                        return;
                    };

                    var parent = selects[0].id;

                    var new_div_with_input = $('<div class="col-md-2" level="'+
                        next_level+'" id="level-'+next_level+'" node_id="'+selects[0]+'">'+
                            '<input class="form-inline"/>'+
                        '</div>');
                    $("#input-holder").append(new_div_with_input);
                    var new_ms = attach_magic_suggest(new_div_with_input, parent);
                    var new_input = $("input", new_div_with_input)[0];
                    setTimeout(function(){
                        $(new_input).focus();
                        ms.collapse();
                    }, 50);

                    console.log(new_input);
            });
            return ms;
        }
        attach_magic_suggest($("#level-0"), null);
    });