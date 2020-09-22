/**
 * Cart handler
 */
var cart_modal_open = false


async function postData(url = '', data = {}) {
    const response = await fetch(`/be/baskets/${url}`, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'same-origin', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data)
    })
    return response.json()
}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = '';


function showSuccessConfirmToast({state, reason, message}){
    iziToast.show({
        theme: 'dark',
        timeout: 20000,
        close: false,
        overlay: true,
        displayMode: 'once',
        id: 'question',
        zindex: 999,
        title: state,
        message: message,
        position: 'center',
        buttons: [
            [`<button><b>CONFIRM</b></button>`, function (instance, toast) {

                instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');

            }, true],
        ],        
    });
}

document.addEventListener('DOMContentLoaded', ev => {
    console.log('cart hooked in ')
    /*      if(window.cart){
             for(let x = 0; x < 10; x++){
                 window.cart.addItem(x)
             }
         } */

    let show_classes = ['is-active is-clipped']
    let isActive = 'is-active'
    let isClipped = 'is-clipped'
    let hide_classes = `modal`

    let cartTriggerBtn = document.querySelector('#modal-cart-trigger')
    let cartModal = document.querySelector('#cart-modal')
    let cartModalClose = document.querySelector('#cart-modal-close')

     csrftoken   = getCookie('csrftoken');

    //server interact button s
    let buyBtn = document.querySelector('#buy-basket'),
        saveBtn = document.querySelector('#save-basket')

    buyBtn.addEventListener('click', ev => {
        console.log('buy items')
        if (window.cart) {
            if (window.cart.ids.length < 1) {

            } else {
                postData('buy', data = window.cart.ids).then(res => {
                    pres = JSON.parse(res)
                    console.log(pres.state)
                    showSuccessConfirmToast(pres)
                }).catch(err => {
                    console.error(err)
                    iziToast.error({
                        title: 'ERROR OCCURED',
                        message: `${err.message}`,
                    });
                })
            }
        }
    })

    if(saveBtn != undefined){
        saveBtn.addEventListener('click', ev => {
            console.log('save items')
            console.log('buy items')
            if (window.cart) {
                if (window.cart.ids.length < 1) {
    
                } else {
                    postData('save', data = window.cart.ids).then(res => {
                        pres = JSON.parse(res)
                        console.log(pres.state)
                        showSuccessConfirmToast(pres)
                    }).catch(err => {
                        console.error(err)
                        iziToast.error({
                            title: 'ERROR OCCURED',
                            message: `${err.message}`,
                        });
                    })
                }
            }
        })
    }


    cartModalClose.addEventListener('click', ev => {
        if (cart_modal_open) {
            console.log('close cart dialog')
            cartModal.classList.remove(isActive)
            cartModal.classList.remove(isClipped)
            cart_modal_open = false
        }
    })

    cartTriggerBtn.addEventListener('click', ev => {

        if (cartModal) {
            if (!cart_modal_open) {
                console.log('open cart dialog')
                cartModal.classList.add(isActive)
                cartModal.classList.add(isClipped)
                cart_modal_open = true
                updateCartCountView()
                fillCartItemsView()
                setTotalPrice()
            } else {
                console.log('close cart dialog')
                cartModal.classList.remove(isActive)
                cartModal.classList.remove(isClipped)
                cart_modal_open = false
            }
        }
    })

    let hideBtn = document.querySelector('.hide-btn')
    hideBtn.addEventListener('click', ev => {
        console.log('hide btn')
        let parent = ev.target.parentNode
        if (parent) {
            parent.style.display = 'none'
        }
    })

    allTotalPriceElements = document.querySelectorAll('.total-cart-price')




    let citInc = document.querySelector('#cit-inc'),
        citDec = document.querySelector('#cit-dec');

    citDec.addEventListener('click', ev => {
        console.log('deduct')
        //this.decrement()
    })
    citInc.addEventListener('click', ev => {
        console.log('Increment')
        //this.increment()
    })



})

var allTotalPriceElements;

function setTotalPrice() {
    let formatedAmount = ''
    if (Intl) {
        var formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',

            // These options are needed to round to whole numbers if that's what you want.
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        });

        formatedAmount = formatter.format(window.cart.totalPrice); /* $2,500.00 */

    }
    allTotalPriceElements.forEach(x => {
        if (window.cart) {
            x.innerHTML = `${formatedAmount}`
        }
    })
}

//prefill cart view elments
function updateCartCountView() {
    if (window.cart) {
        let countDisp = document.querySelectorAll('b.c-count')
        countDisp.forEach(cd => {
            cd.innerHTML = ""
            cd.innerHTML = `${window.cart.getItemCount()}`
        })
    }
}


var cartItemTpl = `
`

function incrementCartItem({ id, max }) {
    //{id: int}

    if (window.cart) {
        let cqty = window.cart.ids[id] || 1
        console.info(`>>> increment1 ${id} | ${max} | current quantity: ${cqty}`)
        if (cqty < max) {
            //this.quantity++
            window.cart.ids[id] += 1
        } else {
            iziToast.error({
                title: 'MAX REACHED',
                message: `We only have ${max} of those`,
            });
        }
        //callback()
        updateCartCountView()
        fillCartItemsView()
        setTotalPrice()
    }
}

function decrementCartItem({ id, max }) {
    //{id: int}

    if (window.cart) {
        let cqty = window.cart.ids[id]
        console.info(`>>> increment1 ${id} | ${max} | current quantity: ${cqty}`)
        if (cqty > 0) {
            //this.quantity++
            window.cart.ids[id] -= 1
        } else {
            //window.cart.ids[id] = 0
            iziToast.error({
                title: 'MIN REACHED',
                message: `None of those have been selected`,
            });
        }
        //callback()
        updateCartCountView()
        fillCartItemsView()
        setTotalPrice()
    }
}

function CartItem(item = { quantity: 0 }) {
    this.item = item
    this.quantity = 0;
    if (window.cart) {
        this.quantity = window.cart.ids[parseInt(item.id)]
    }

    this.totalPrice = function () {
        let tp = this.quantity * (parseFloat(this.item.cost) || 0)
        if (window.cart) {
            window.cart.totalPrice += tp
        }
        return tp
    }


    this.tpl = `<tr>
                            <td>${item.name}</td>
                            <td>${item.cost}</td>
                            <td>${this.quantity}</td>
                            <td>${this.totalPrice()}</td>
                            <td>${this.isAvail ? 'yes' : 'no'}</td>
                            <td>
                                <div class="field has-addons">
                                    <p class="control">
                                        <button onclick="incrementCartItem({id:${item.id}, max:${item.quantity}})" class="button is-primary  is-small">                                            
                                            <span>Add</span>
                                        </button>
                                    </p>
                                    <p class="control">
                                        <button onclick="decrementCartItem({id:${item.id}, max:${item.quantity}})" id="cit-inc" class="button  is-small">                                            
                                            <span>Deduct</span>
                                        </button>
                                    </p>
                                    <p class="control">
                                        <button id="cit-dec" class="button is-danger is-small">                                            
                                            <span>Delete</span>
                                        </button>
                                    </p>
                                </div>
                            </td>

                        </tr>`


    this.getNode = function () {
        return this.tpl
    }



    this.emitCustomClickEvent = function (evName = '', data = {}) {
        const ev = new CustomEvent(evName, {
            bubbles: true,
            detail: { ...data }
        });
    }

    this.increment = function () {
        console.info('>>> increment')
        if (this.quantity < item.quantity) {
            this.quantity++
        }
    }

    this.decrement = function () {
        console.info('>>> decrement')
        if (this.quantity > 0) {
            this.quantity--
        } else {
            this.quantity = 0
        }
    }


    this.initHandlers = function () {
        /*         citDec.addEventListener('click', ev => {
                    console.log('deduct')
                    this.decrement()
                })
                citInc.addEventListener('click', ev => {
                    console.log('Increment')
                    this.increment()
                }) */
    }

    this.initHandlers()

    return this
}

function fillCartItemsView() {
    //console.info('fill cart items')
    //let area = document.querySelector('.mcb-articles')
    let area = document.querySelector('tbody#items-table-body')        
    if (area) {
        //area.innerHTML = ''
        if (window.cart) {
            let out = '', i = 0
            if (prevCount < window.cart.getItemCount()) {
                window.cart.totalPrice = 0
                window.cart.getItems().forEach((entry) => {
                    i++;
                    ct = CartItem(entry)
                    console.log(ct)
                    out += ct.getNode()
                })
                console.log(out)
                area.innerHTML = out
            } else if (prevCount > window.cart.getItemCount()) {
                window.cart.totalPrice = 0
                window.cart.getItems().forEach((entry) => {
                    i++;
                    ct = CartItem(entry)
                    console.log(ct)
                    out += ct.getNode()
                })
                console.log(out)
                area.innerHTML = out
            }
        } else {
            
        }
    }
}

var prevCount = 0


function Cart() {
    this.items = new Array()
    this.ids = {}
    this.user = undefined
    this.session = undefined
    this.totalPrice = 0;

    this.getItemCount = () => this.items.length;

    this.getItems = () => this.items;
    this.getUser = () => this.user
    this.getSession = () => this.session

    this.addItem = item => {
        this.items.push(item)
    }
    this.browserStorage = (win) => {
        //TODO
    }

    //Uneficient algorithm
    this.distinctItems = function () {
        const resutls = Array.from(new Set(this.items.map(i => i.id)))
            .map(id => {
                return (this.items.find(x => x.id === id))


            })
    }
}




//Cart.prototype.getItemCount = () => this.items.length()


window.cart = new Cart()


