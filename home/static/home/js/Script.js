const name=document.getElementById('name')
const password=document.getElementById('password')
const form=document.getElementById('form')
const errorElement=document.getElementById('error')

form.addEventListener('submit',(e)=>{
    let messages=[]
    if (name.value ===''||name.value ==null){
        messages.push('name is required')

    }
    if (password.value ===''||password.value ==null){
        messages.push('password is required')
         }
    if (password.value <= 6){
        messages.push('password must be longer than 6 characters')
         }
    if (password.value >=15){

        messages.push('password must be less than 15 characters')

    } if (messages.length>0){
        e.preventDefault()
        errorElement.innerText =messages.join(' ,and ')
        }
})
