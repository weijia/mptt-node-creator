$(function() {
        function gen_parent_param_dict(parent){

            var additionalParam = {};
            additionalParam[parent_name] = root_parent;
            if(parent){
                additionalParam[parent_name] = parent;
            }
            return additionalParam;
        }
        function attach_magic_suggest(div_elem, parent){
            var elem = $("input", div_elem);

            var ms = elem.magicSuggest({
                data: base_tree_url,
                resultsField: results_field,
                valueField: "id",
                displayField: display_field,
                dataUrlParams: gen_parent_param_dict(parent),
                queryParam: query_param,
                method: "GET"
            });
            div_elem.attr("ms", ms);
            $(ms).on("selectionchange", function(e, control, selects){
                    console.log(ms);
                    var parent = selects[0].id;

                    if(selects.length == 0){
                        return;
                    }

                    var next_level = parseInt(div_elem.attr("level"))+1;
                    var next_level_div_elem = $("#level-"+next_level);
                    var next_ms = next_level_div_elem.attr("ms");
                    if(next_level_div_elem.length > 0){
                        setTimeout(function(){
                            console.log("focus on", $("input", next_level_div_elem));
                            $("input", next_level_div_elem).focus();
                            next_ms.setDataUrlParams(gen_parent_param_dict(parent));
                        }, 50);
                        return;
                    };

                    var new_div_with_input = $('<div class="col-md-2" level="'+
                        next_level+'" id="level-'+next_level+'" node_id="'+selects[0].id+'">'+
                            '<input class="form-inline" name="level'+next_level+'" />'+
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
        attach_magic_suggest($("#level-0"), false);
    });