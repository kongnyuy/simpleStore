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

    //prefill cart view elments
    function updateCartCountView() {
        if (window.cart) {
            let countDisp = document.querySelector('b.c-count')
            countDisp.innerHTML = ""
            countDisp.innerHTML = `${window.cart.getItemCount()}`
        }
    }

})

var cartItemTpl = `
`

function fillCartItemsView() {
    console.info('fill cart items')
    let area = document.querySelector('.mcb-articles')
    if (area) {
        area.innerHTML = ''
        if (window.cart) {
            let out = '', i = 0        
            window.cart.getItems().forEach((entry) => {
                i++;
                out += `<div key=${i} class="cit">
    <div class="cit-val">
        <b class="cit-val-name">${entry.name}</b>
    </div>
    <div class="cit-controls">        
        <button class="button is-danger ">
            <span class="icon is-small">
                <i class=" gg-add"></i>
            </span>
        </button>
        <b id="cit-count">100</b>
        <button class="button is-info ">
            <span class="icon is-small">
                <i class=" gg-remove"></i>                
            </span>
        </button>
    </div>
</div>`
            })
            console.log(out)
            area.innerHTML = out
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


