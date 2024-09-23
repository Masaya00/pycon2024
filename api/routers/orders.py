from ninja import Router

router: Router = Router()


@router.get("")
def list_products(request):
    return {"message": "List of products"}
