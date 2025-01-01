
Cart = function (params) {

    var self = this,
        $body = $('body');

    var modal = new Modal({
        url: params.urls.modal,
        selector: '[data-role=open-cart-btn]',
    });

    function handleAddBtnClick() {
        var $btn = $(this),
            productId = $btn.data('product-id');

        toggleAddBtn(productId, false);

        self.beforeAdd($btn).done(function () {
            $.post(
                params.urls.add,
                {
                    csrfmiddlewaretoken: csrf,
                    product: productId
                },
                function (response) {
                    handleSaveSuccess(response);
                    modal.show();
                    $(window).trigger("cart.added", [response.result]);
                }
            ).fail(function (response) {
                toggleAddBtn(productId, true);
                handleSaveError(response);
            });
        }).fail(function () {
            toggleAddBtn(productId, true);
        });
    }

    function handleRemoveBtnClick() {
        var productId = $(this).data('product-id');

        $(this).closest('[data-role=cart-item]').remove();

        toggleAddBtn(productId, true);

        $.post(
            params.urls.remove,
            {
                csrfmiddlewaretoken: csrf,
                product: productId
            },
            (response) => {
                handleSaveSuccess(response);
                $(window).trigger("cart.removed", [response.result]);
            }
        );
    }

    function handleQtyChange () {

        var productId = $(this).data('product-id'),
            maxQty = $(this).prop('max'),
            qty = parseInt($(this).val());

        if (qty < 1) {
            qty = 1;
            $(this).val(qty);
        }

        if (maxQty && qty > maxQty) {
            qty = maxQty;
            $(this).val(qty);
        }

        return $.post(
            params.urls.setQty,
            {
                csrfmiddlewaretoken: csrf,
                product: productId,
                qty: qty
            },
            function (response) {
                handleSaveSuccess(response);
                updateItemTotal(productId, response.result.total);
            });
    }

    function updateItemTotal(productId, total) {
        $('[data-role=cart-item-total]')
            .filter('[data-product-id=' + productId + ']')
            .text(total);
    }

    function handlePlusQtyBtnClick() {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1).trigger('input');
    }

    function handleMinusQtyBtnClick() {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) - 1).trigger('input');
    }

    function handleSaveSuccess(response) {
        $('[data-role=cart-total]').text(response.total);
        $.notify({message: response.message}, {type: 'success'});
    }

    function toggleAddBtn(productId, isEnabled) {
        $('[data-role=add-to-cart]')
            .filter('[data-product-id=' + productId + ']')
            .prop('disabled', !isEnabled);
    }

    function handleSaveError(response) {
        $.notify({
            message: response.responseJSON.message
        }, {
            type: 'danger'
        });
    }

    this.beforeAdd = function ($btn) {
        return $.Deferred().resolve().promise();
    };

    $body.on('click', '[data-role=add-to-cart]', handleAddBtnClick);
    $body.on('click', '[data-role=remove-from-cart]', handleRemoveBtnClick);
    $body.on('input', '[data-role=cart-item-qty]', handleQtyChange);
    $body.on('click', '[data-role=plus-cart-item-qty]', handlePlusQtyBtnClick);
    $body.on('click', '[data-role=minus-cart-item-qty]', handleMinusQtyBtnClick);

};
