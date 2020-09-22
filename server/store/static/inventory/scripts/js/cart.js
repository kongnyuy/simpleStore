/**
 * Cart handler
 */
var cart_modal_open = false
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
        if(parent){
            parent.style.display = 'none'
        }
    })

    //prefill cart view elments
    function updateCartCountView() {
        if (window.cart) {
            let countDisp = document.querySelector('b.c-count')
            countDisp.innerHTML = ""
            countDisp.innerHTML = `${window.cart.getItemCount()}`
        }
    }


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

var cartItemTpl = `
`

function CartItem(item = { quantity: 0 }) {
    this.item = item
    this.quantity = parseInt(this.item.quantity)

    this.totalPrice = function () {
        return this.quantity * (parseFloat(this.item.cost) || 0)
    }

   
    this.tpl = `<tr>
                            <td>${item.name}</td>
                            <td>${item.cost}</td>
                            <td>${item.quantity}</td>
                            <td>${this.totalPrice()}</td>
                            <td>${this.isAvail ? 'yes' : 'no'}</td>
                            <td>
                                <div class="field has-addons">
                                    <p class="control">
                                        <button class="button is-primary  is-small">                                            
                                            <span>Add</span>
                                        </button>
                                    </p>
                                    <p class="control">
                                        <button id="cit-inc" class="button  is-small">                                            
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
    


    this.emitCustomClickEvent = function(evName = '', data = {}){
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
    console.info('fill cart items')
    //let area = document.querySelector('.mcb-articles')
    let area = document.querySelector('tbody#items-table-body')
    console.log(area)
    if (area) {
        //area.innerHTML = ''
        if (window.cart) {
            let out = '', i = 0
            window.cart.getItems().forEach((entry) => {
                i++;
                ct = CartItem(entry)
                console.log(ct)
                out += ct.getNode()
            })
            console.log(out)
            area.innerHTML = out
        }else{
            console.error('not there')
        }
    }
}


function Cart() {
    this.items = new Set()
    this.user = undefined
    this.session = undefined

    this.getItemCount = () => this.items.size;

    this.getItems = () => this.items;
    this.getUser = () => this.user
    this.getSession = () => this.session

    this.addItem = item => {
        this.items.add(item)
    }
    this.browserStorage = (win) => {
        //TODO
    }
}




//Cart.prototype.getItemCount = () => this.items.length()


window.cart = new Cart()


