let params = `scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,
width=800,height=560,left=100,top=100`;

let url = document.getElementById("two")

document.getElementById("one").onclick = () => {
    open(url, 'test', params);
};