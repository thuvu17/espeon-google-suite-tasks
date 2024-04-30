window.addEventListener('load',()=>{
    const form = document.querySelector("#new-task-form");
    const input = document.querySelector("#new-task-input");
    const list_element = document.querySelector("#tasks");

    form.addEventListener('submit', (e)=>{
        e.preventDefault();

        const task=input.ariaValueMax;

        if (!task){
            alert("Please fill out the task");
        } else {
            console.log("Submitted");
            return;
        }
    })
})