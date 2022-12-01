$(document).ready(function () {

    $(".delete").click(function (e) { 
        let sno = Number($(this).attr("id"));
        console.log(sno)
        e.preventDefault();
        $.ajax({
            url: "/delete/"+sno,
            success: function (response) {
                
            }
        });
        $("#task"+sno).fadeOut(300);
    });


    $(".completed").click(function (e) { 
        let sno = Number($(this).attr("id"));
        let title = $("#title"+sno).text()
        console.log(sno)
        e.preventDefault();
        $.ajax({
            url: "/completed/"+sno,
            success: function (response) {
                
            }
        });
        $("#completed"+sno).html(`<div class="inline-flex items-center space-x-2">
        <div id="{{i.sno}}" class="completed">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                    stroke="green" class="w-6 h-6 text-slate-500">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
        </div>
        <div id="title{{i.sno}}" class="text-slate-500 line-through decoration-green-400 decoration-2 px-2 overflow-hidden ">${title}</div>
    </div>`)
        
        
        
    });
});

