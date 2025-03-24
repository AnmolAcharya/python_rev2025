async function greet(){

    let name = "David"

    let greeting = "Welcome " + name 
    return  greeting
}

// console.log(greet())

async function main(){
    console.log(await greet())
}

main()





