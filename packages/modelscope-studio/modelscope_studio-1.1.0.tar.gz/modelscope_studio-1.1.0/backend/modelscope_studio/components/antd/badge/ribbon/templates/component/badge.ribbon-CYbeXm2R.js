import { i as se, a as j, r as ie, g as le, w as O } from "./Index-hlxiuCED.js";
const E = window.ms_globals.React, te = window.ms_globals.React.forwardRef, ne = window.ms_globals.React.useRef, re = window.ms_globals.React.useState, oe = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, ae = window.ms_globals.internalContext.useContextPropsContext, ce = window.ms_globals.antd.Badge;
var ue = /\s/;
function de(e) {
  for (var t = e.length; t-- && ue.test(e.charAt(t)); )
    ;
  return t;
}
var fe = /^\s+/;
function me(e) {
  return e && e.slice(0, de(e) + 1).replace(fe, "");
}
var F = NaN, pe = /^[-+]0x[0-9a-f]+$/i, _e = /^0b[01]+$/i, he = /^0o[0-7]+$/i, ge = parseInt;
function M(e) {
  if (typeof e == "number")
    return e;
  if (se(e))
    return F;
  if (j(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = j(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = me(e);
  var o = _e.test(e);
  return o || he.test(e) ? ge(e.slice(2), o ? 2 : 8) : pe.test(e) ? F : +e;
}
var P = function() {
  return ie.Date.now();
}, be = "Expected a function", ye = Math.max, Ee = Math.min;
function we(e, t, o) {
  var i, s, n, r, l, u, p = 0, g = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(be);
  t = M(t) || 0, j(o) && (g = !!o.leading, a = "maxWait" in o, n = a ? ye(M(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(d) {
    var y = i, R = s;
    return i = s = void 0, p = d, r = e.apply(R, y), r;
  }
  function w(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var y = d - u, R = d - p, D = t - y;
    return a ? Ee(D, n - R) : D;
  }
  function _(d) {
    var y = d - u, R = d - p;
    return u === void 0 || y >= t || y < 0 || a && R >= n;
  }
  function h() {
    var d = P();
    if (_(d))
      return x(d);
    l = setTimeout(h, f(d));
  }
  function x(d) {
    return l = void 0, b && i ? m(d) : (i = s = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), p = 0, i = u = s = l = void 0;
  }
  function c() {
    return l === void 0 ? r : x(P());
  }
  function C() {
    var d = P(), y = _(d);
    if (i = arguments, s = this, u = d, y) {
      if (l === void 0)
        return w(u);
      if (a)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return C.cancel = v, C.flush = c, C;
}
var X = {
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
var xe = E, ve = Symbol.for("react.element"), Ce = Symbol.for("react.fragment"), Ie = Object.prototype.hasOwnProperty, Re = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Se = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Y(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Ie.call(t, i) && !Se.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: ve,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Re.current
  };
}
L.Fragment = Ce;
L.jsx = Y;
L.jsxs = Y;
X.exports = L;
var S = X.exports;
const {
  SvelteComponent: Oe,
  assign: U,
  binding_callbacks: z,
  check_outros: Te,
  children: Q,
  claim_element: Z,
  claim_space: ke,
  component_subscribe: G,
  compute_slots: Le,
  create_slot: Pe,
  detach: I,
  element: $,
  empty: H,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Ne,
  get_slot_changes: Ae,
  group_outros: je,
  init: We,
  insert_hydration: T,
  safe_not_equal: Be,
  set_custom_element_data: ee,
  space: De,
  transition_in: k,
  transition_out: W,
  update_slot_base: Fe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Me,
  getContext: Ue,
  onDestroy: ze,
  setContext: Ge
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Pe(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = $("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = Z(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Q(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      ee(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Fe(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Ae(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ne(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (k(s, n), o = !0);
    },
    o(n) {
      W(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function He(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = $("react-portal-target"), o = De(), n && n.c(), i = H(), this.h();
    },
    l(r) {
      t = Z(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Q(t).forEach(I), o = ke(r), n && n.l(r), i = H(), this.h();
    },
    h() {
      ee(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, o, l), n && n.m(r, l), T(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = q(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (je(), W(n, 1, 1, () => {
        n = null;
      }), Te());
    },
    i(r) {
      s || (k(n), s = !0);
    },
    o(r) {
      W(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function V(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ke(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Le(n);
  let {
    svelteInit: u
  } = t;
  const p = O(V(t)), g = O();
  G(e, g, (c) => o(0, i = c));
  const a = O();
  G(e, a, (c) => o(1, s = c));
  const b = [], m = Ue("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = le() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: a,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      b.push(c);
    }
  });
  Ge("$$ms-gr-react-wrapper", h), Me(() => {
    p.set(V(t));
  }), ze(() => {
    b.forEach((c) => c());
  });
  function x(c) {
    z[c ? "unshift" : "push"](() => {
      i = c, g.set(i);
    });
  }
  function v(c) {
    z[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = U(U({}, t), K(c))), "svelteInit" in c && o(5, u = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = K(t), [i, s, g, a, l, u, r, n, x, v];
}
class qe extends Oe {
  constructor(t) {
    super(), We(this, t, Ke, He, Be, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ve(e, t = {}) {
  function o(i) {
    const s = O(), n = new qe({
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
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], J({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== s), J({
              createPortal: A,
              node: N
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
const Je = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Xe(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = Ye(o, i), t;
  }, {}) : {};
}
function Ye(e, t) {
  return typeof t == "number" && !Je.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = B(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(A(E.cloneElement(e._reactElement, {
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
      } = B(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function Qe(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Ze = te(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ne(), [l, u] = re([]), {
    forceClone: p
  } = ae(), g = p ? !0 : t;
  return oe(() => {
    var w;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Qe(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = Xe(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, c, C;
        (v = r.current) != null && v.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: x
        } = B(e);
        a = x, u(h), a.style.display = "contents", b(), (C = r.current) == null || C.appendChild(a);
      };
      f();
      const _ = we(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", b(), (w = r.current) == null || w.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Ve(({
  slots: e,
  children: t,
  ...o
}) => /* @__PURE__ */ S.jsx(S.Fragment, {
  children: /* @__PURE__ */ S.jsx(ce.Ribbon, {
    ...o,
    text: e.text ? /* @__PURE__ */ S.jsx(Ze, {
      slot: e.text
    }) : o.text,
    children: t
  })
}));
export {
  et as BadgeRibbon,
  et as default
};
