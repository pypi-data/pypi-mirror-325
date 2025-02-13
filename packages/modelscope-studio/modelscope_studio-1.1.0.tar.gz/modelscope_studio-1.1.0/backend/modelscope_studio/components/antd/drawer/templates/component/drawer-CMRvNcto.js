import { i as ue, a as A, r as de, g as fe, w as T, b as me } from "./Index-BUIeL3RV.js";
const y = window.ms_globals.React, se = window.ms_globals.React.forwardRef, ie = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ce = window.ms_globals.React.useEffect, ae = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, _e = window.ms_globals.internalContext.useContextPropsContext, z = window.ms_globals.internalContext.ContextPropsProvider, pe = window.ms_globals.antd.Drawer;
var he = /\s/;
function ge(e) {
  for (var t = e.length; t-- && he.test(e.charAt(t)); )
    ;
  return t;
}
var we = /^\s+/;
function be(e) {
  return e && e.slice(0, ge(e) + 1).replace(we, "");
}
var B = NaN, xe = /^[-+]0x[0-9a-f]+$/i, ye = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ve = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return B;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var o = ye.test(e);
  return o || Ee.test(e) ? ve(e.slice(2), o ? 2 : 8) : xe.test(e) ? B : +e;
}
var j = function() {
  return de.Date.now();
}, Ce = "Expected a function", Ie = Math.max, Re = Math.min;
function Se(e, t, o) {
  var i, s, n, r, l, u, _ = 0, g = !1, c = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = G(t) || 0, A(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Ie(G(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(d) {
    var b = i, S = s;
    return i = s = void 0, _ = d, r = e.apply(S, b), r;
  }
  function E(d) {
    return _ = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var b = d - u, S = d - _, U = t - b;
    return c ? Re(U, n - S) : U;
  }
  function p(d) {
    var b = d - u, S = d - _;
    return u === void 0 || b >= t || b < 0 || c && S >= n;
  }
  function h() {
    var d = j();
    if (p(d))
      return v(d);
    l = setTimeout(h, f(d));
  }
  function v(d) {
    return l = void 0, w && i ? m(d) : (i = s = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), _ = 0, i = u = s = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(j());
  }
  function I() {
    var d = j(), b = p(d);
    if (i = arguments, s = this, u = d, b) {
      if (l === void 0)
        return E(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return I.cancel = C, I.flush = a, I;
}
var $ = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = y, Te = Symbol.for("react.element"), ke = Symbol.for("react.fragment"), Pe = Object.prototype.hasOwnProperty, Le = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ee(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Pe.call(t, i) && !je.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Te,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Le.current
  };
}
L.Fragment = ke;
L.jsx = ee;
L.jsxs = ee;
$.exports = L;
var x = $.exports;
const {
  SvelteComponent: Fe,
  assign: H,
  binding_callbacks: K,
  check_outros: Ne,
  children: te,
  claim_element: ne,
  claim_space: We,
  component_subscribe: q,
  compute_slots: Ae,
  create_slot: De,
  detach: R,
  element: re,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Me,
  get_slot_changes: Ue,
  group_outros: ze,
  init: Be,
  insert_hydration: k,
  safe_not_equal: Ge,
  set_custom_element_data: oe,
  space: He,
  transition_in: P,
  transition_out: D,
  update_slot_base: Ke
} = window.__gradio__svelte__internal, {
  beforeUpdate: qe,
  getContext: Ve,
  onDestroy: Je,
  setContext: Xe
} = window.__gradio__svelte__internal;
function X(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = De(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = re("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ne(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = te(t);
      s && s.l(r), r.forEach(R), this.h();
    },
    h() {
      oe(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ke(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Ue(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Me(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(s, n), o = !0);
    },
    o(n) {
      D(s, n), o = !1;
    },
    d(n) {
      n && R(t), s && s.d(n), e[9](null);
    }
  };
}
function Ye(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = re("react-portal-target"), o = He(), n && n.c(), i = V(), this.h();
    },
    l(r) {
      t = ne(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), te(t).forEach(R), o = We(r), n && n.l(r), i = V(), this.h();
    },
    h() {
      oe(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && P(n, 1)) : (n = X(r), n.c(), P(n, 1), n.m(i.parentNode, i)) : n && (ze(), D(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      s || (P(n), s = !0);
    },
    o(r) {
      D(n), s = !1;
    },
    d(r) {
      r && (R(t), R(o), R(i)), e[8](null), n && n.d(r);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Qe(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ae(n);
  let {
    svelteInit: u
  } = t;
  const _ = T(Y(t)), g = T();
  q(e, g, (a) => o(0, i = a));
  const c = T();
  q(e, c, (a) => o(1, s = a));
  const w = [], m = Ve("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: p
  } = fe() || {}, h = u({
    parent: m,
    props: _,
    target: g,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: p,
    onDestroy(a) {
      w.push(a);
    }
  });
  Xe("$$ms-gr-react-wrapper", h), qe(() => {
    _.set(Y(t));
  }), Je(() => {
    w.forEach((a) => a());
  });
  function v(a) {
    K[a ? "unshift" : "push"](() => {
      i = a, g.set(i);
    });
  }
  function C(a) {
    K[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = H(H({}, t), J(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = J(t), [i, s, g, c, l, u, r, n, v, C];
}
class Ze extends Fe {
  constructor(t) {
    super(), Be(this, t, Qe, Ye, Ge, {
      svelteInit: 5
    });
  }
}
const Q = window.ms_globals.rerender, F = window.ms_globals.tree;
function $e(e, t = {}) {
  function o(i) {
    const s = T(), n = new Ze({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? F;
          return u.nodes = [...u.nodes, l], Q({
            createPortal: W,
            node: F
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== s), Q({
              createPortal: W,
              node: F
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = nt(o, i), t;
  }, {}) : {};
}
function nt(e, t) {
  return typeof t == "number" && !et.includes(e) ? t + "px" : t;
}
function M(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = M(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = M(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function rt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const O = se(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ie(), [l, u] = le([]), {
    forceClone: _
  } = _e(), g = _ ? !0 : t;
  return ce(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), o && f.classList.add(...o.split(" ")), i) {
        const p = tt(i);
        Object.keys(p).forEach((h) => {
          f.style[h] = p[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, a, I;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: v
        } = M(e);
        c = v, u(h), c.style.display = "contents", w(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const p = Se(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(p), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var f, p;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((p = r.current) == null || p.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function st(e, t = !1) {
  try {
    if (me(e))
      return e;
    if (t && !ot(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function N(e, t) {
  return ae(() => st(e, t), [e, t]);
}
function Z(e, t) {
  return e ? /* @__PURE__ */ x.jsx(O, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function it({
  key: e,
  slots: t,
  targets: o
}, i) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ x.jsx(z, {
    params: s,
    forceClone: !0,
    children: Z(n, {
      clone: !0,
      ...i
    })
  }, r)) : /* @__PURE__ */ x.jsx(z, {
    params: s,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...i
    })
  }) : void 0;
}
const ct = $e(({
  slots: e,
  afterOpenChange: t,
  getContainer: o,
  drawerRender: i,
  setSlotParams: s,
  ...n
}) => {
  const r = N(t), l = N(o), u = N(i);
  return /* @__PURE__ */ x.jsx(pe, {
    ...n,
    afterOpenChange: r,
    closeIcon: e.closeIcon ? /* @__PURE__ */ x.jsx(O, {
      slot: e.closeIcon
    }) : n.closeIcon,
    extra: e.extra ? /* @__PURE__ */ x.jsx(O, {
      slot: e.extra
    }) : n.extra,
    footer: e.footer ? /* @__PURE__ */ x.jsx(O, {
      slot: e.footer
    }) : n.footer,
    title: e.title ? /* @__PURE__ */ x.jsx(O, {
      slot: e.title
    }) : n.title,
    drawerRender: e.drawerRender ? it({
      slots: e,
      setSlotParams: s,
      key: "drawerRender"
    }) : u,
    getContainer: typeof o == "string" ? l : o
  });
});
export {
  ct as Drawer,
  ct as default
};
